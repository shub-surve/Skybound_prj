from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from razorpay import Client
from django.conf import settings
from bookings.models import Event_Booking, Course_Booking
from payments.models import EventPayment , CoursePayment



from events.views import generate_pdf
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from io import BytesIO
import logging


from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)



import logging
logger = logging.getLogger(__name__)



# Razorpay Client
razorpay_client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_KEY_SECRET))



def event_payment_view(request, booking_id):
    booking = get_object_or_404(Event_Booking, id=booking_id)

    if booking.payment_status == "Paid":
        return JsonResponse({'status': 'error', 'message': 'Payment already completed for this booking.'})

    # Calculate amount
    amount = int(booking.event.registration_amt * 100)  # Convert to paise

    # Create Razorpay order
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': f'order_rcptid_{booking_id}',
    }
    razorpay_order = razorpay_client.order.create(data=order_data)

    # Save payment instance
    payment = EventPayment.objects.create(
        booking=booking,
        order_id=razorpay_order['id'],
        amount=amount // 100,  # INR for display
        currency='INR',
        status='Created',
    )

    # Render Razorpay payment page
    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_api_key': settings.RAZORPAY_API_KEY,
        'booking': booking,
        'amount': amount // 100,
    }

    return render(request, 'event_payment_page.html', context)


def course_payment_view(request, booking_id):
    booking = get_object_or_404(Course_Booking, id=booking_id)

    if booking.payment_status == "Paid":
        return JsonResponse({'status': 'error', 'message': 'Payment already completed for this booking.'})

    # Calculate amount
    amount = booking.course.registration_fees * 100  # Convert to paise

    # Create Razorpay order
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': f'order_rcptid_{booking_id}',
    }
    razorpay_order = razorpay_client.order.create(data=order_data)

    # Save payment instance
    payment = CoursePayment.objects.create(
        booking=booking,
        order_id=razorpay_order['id'],
        amount=amount / 100,
        currency='INR',
        status='Created',
    )

    # Render Razorpay payment page
    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_api_key': settings.RAZORPAY_API_KEY,
        'booking': booking,
        'amount': amount / 100,
    }

    return render(request, 'course_payment.html', context)

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.http import JsonResponse

def send_event_confirmation_email(booking, booking_name):
    subject = f"Registration Confirmation for Event: {booking_name}"
    email_body = f"Dear {booking.user.username},\n\nThank you for registering for the event: {booking_name}.\n\nRegards,\nSkybound Team"

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email='your_email@example.com',
        to=[booking.user.email],
    )
    email.send()

def send_course_confirmation_email(booking, booking_name):
    subject = f"Registration Confirmation for Course: {booking_name}"
    email_body = f"Dear {booking.user.username},\n\nThank you for registering for the course: {booking_name}.\n\nRegards,\nSkybound Team"

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email='your_email@example.com',
        to=[booking.user.email],
    )
    email.send()

def payment_callback(request):
    if request.method == 'POST':
        data = request.POST
        order_id = data.get('razorpay_order_id')
        payment_id = data.get('razorpay_payment_id')
        signature = data.get('razorpay_signature')

        try:
            # Verify the payment signature
            razorpay_client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            })

            # Initialize variables
            payment = None
            booking = None
            booking_type = None
            booking_name = None

            # Check for EventPayment or CoursePayment based on order_id
            if EventPayment.objects.filter(order_id=order_id).exists():
                payment = EventPayment.objects.get(order_id=order_id)
                booking = payment.booking  # Booking for Event
                booking_type = 'event'
                booking_name = booking.event.name  # Event name for email
            elif CoursePayment.objects.filter(order_id=order_id).exists():
                payment = CoursePayment.objects.get(order_id=order_id)
                booking = payment.booking  # Booking for Course
                booking_type = 'course'
                booking_name = booking.course.course_name  # Course name for email
            else:
                raise ValueError("Order not found in either EventPayment or CoursePayment.")

            # Ensure that booking and payment are both found
            if not payment or not booking:
                raise ValueError("Payment or booking data is missing.")

            # Update payment details
            payment.payment_id = payment_id
            payment.signature = signature
            payment.status = 'Success'
            payment.save()

            # Update booking status
            booking.payment_status = 'Paid'
            booking.save()

            # Send confirmation email based on booking type
            if booking_type == 'event':
                send_event_confirmation_email(booking, booking_name)
            elif booking_type == 'course':
                send_course_confirmation_email(booking, booking_name)

            return redirect('home')  # Redirect to the home page after processing

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Payment verification failed.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})