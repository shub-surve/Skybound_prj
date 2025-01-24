from django.shortcuts import render, get_object_or_404 , redirect   
from django.http import JsonResponse
from razorpay import Client
from django.conf import settings
from .models import Event_Booking, EventPayment , Course_Booking , CoursePayment

# Razorpay Client
razorpay_client = Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_KEY_SECRET))


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
        'razorpay_api_key': 'your_api_key',
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
        'razorpay_api_key': 'your_api_key',
        'booking': booking,
        'amount': amount / 100,
    }
    return render(request, 'course_payment.html', context)

import logging


logger = logging.getLogger(__name__)

def payment_callback(request):
    if request.method == 'POST':
        data = request.POST
        order_id = data.get('razorpay_order_id')
        payment_id = data.get('razorpay_payment_id')
        signature = data.get('razorpay_signature')

        logger.info(f"Received payment callback with Order ID: {order_id}, Payment ID: {payment_id}, Signature: {signature}")

        try:
            # Verify the payment signature
            razorpay_client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            })

            # Check which model the order belongs to
            if EventPayment.objects.filter(order_id=order_id).exists():
                payment = EventPayment.objects.get(order_id=order_id)
            elif CoursePayment.objects.filter(order_id=order_id).exists():
                payment = CoursePayment.objects.get(order_id=order_id)
            else:
                raise Exception("Order not found in either EventPayment or CoursePayment.")

            # Update payment details
            payment.payment_id = payment_id
            payment.signature = signature
            payment.status = 'Success'
            payment.save()

            # Update booking status
            booking = payment.booking
            booking.payment_status = 'Paid'
            
            booking.save()

            return redirect('home')  # Redirect to a success page

        except Exception as e:
            logger.error(f"Payment verification failed: {e}")
            return JsonResponse({'status': 'error', 'message': 'Payment verification failed.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})