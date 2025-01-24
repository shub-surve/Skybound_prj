
from .models import Event_Booking , Course_Booking
def send_event_registration_email(booking, razorpay_order_id, amount):
    """
    Sends an email to the user after successful registration for an event,
    attaching the invoice as a PDF.
    """
    if isinstance(booking, Event_Booking):
        subject = f"Registration Confirmation for Event: {booking.event.name}"
        booking_name = booking.event.name
    else:
        raise ValueError("Invalid booking type. Expected Event_Booking.")

    # Email content
    context = {
        'razorpay_order_id': razorpay_order_id,
        'booking': booking,
        'amount': amount / 100,  # Convert to INR for readability
    }

    # Generate PDF invoice
   


def send_course_registration_email(booking, razorpay_order_id, amount):
    """
    Sends an email to the user after successful registration for a course,
    attaching the invoice as a PDF.
    """
    if isinstance(booking, Course_Booking):
        subject = f"Registration Confirmation for Course: {booking.course.name}"
        booking_name = booking.course.name
    else:
        raise ValueError("Invalid booking type. Expected Course_Booking.")

    # Email content
    context = {
        'razorpay_order_id': razorpay_order_id,
        'booking': booking,
        'amount': amount / 100,  # Convert to INR for readability
    }

    # Generate PDF invoice
   
