from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import Event_Booking_Form, Course_Booking_Form
from .models import Event_Booking, Course_Booking
from events.models import Event, CourseDetails
from django.contrib import messages


def event_booking_view(request, id):
    """
    View for booking an event. Redirects to the payment page upon successful booking.
    """
    user = request.user  # Get the currently logged-in user
    event = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        form = Event_Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.user = user
            booking.save()  # Save the booking
            
            # Decrease event capacity
            if event.capacity > 0:
                event.capacity -= 1
                event.save()
            else:
                messages.error(request, "Sorry, no more slots are available for this event.")
                return redirect(reverse('events:event_list'))

            messages.success(request, "Booking successful! Redirecting to payment.")
            return redirect(reverse('payments:event_payment', args=[booking.id]))
        else:
            messages.error(request, "There was an error with your booking form. Please try again.")
    else:
        form = Event_Booking_Form()

    return render(request, 'event_booking.html', {'form': form, 'event': event})


def course_booking_view(request, id):
    """
    View for booking a course. Redirects to the payment page upon successful booking.
    """
    user = request.user  # Get the currently logged-in user
    course = get_object_or_404(CourseDetails, pk=id)

    if request.method == 'POST':
        form = Course_Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.course = course
            booking.user = user
            print(booking)
            booking.save()  # Save the booking

            messages.success(request, "Course booking successful! Redirecting to payment.")
            return redirect(reverse('payments:course_payment', args=[booking.id]))
        else:
            messages.error(request, "There was an error with your booking form. Please try again.")
    else:
        form = Course_Booking_Form()

    return render(request, 'course_booking.html', {'form': form, 'course': course})
