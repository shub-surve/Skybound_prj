from django.shortcuts import render , get_object_or_404
from .forms import Event_Booking_Form , Course_Booking_Form
from .models import Event_Booking , Course_Booking
from events.models import Event , CourseDetails
from django.contrib.contenttypes.models import ContentType
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .forms import Event_Booking_Form
from .models import Event


def event_booking_view(request, id):
    """
    Handles event booking.
    """
    event = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        form = Event_Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return render(request, 'event_booking.html', {'form': form, 'event': event, 'booking': booking})
    else:
        form = Event_Booking_Form()

    return render(request, 'event_booking.html', {'form': form, 'event': event})



def course_booking_view(request, id):
    event = get_object_or_404(CourseDetails, pk=id)
    if request.method == 'POST':
        form = Course_Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
        
        event_content = ContentType.objects.get_for_model(event)
    else:
        form = Event_Booking_Form()
    return render(request, 'event_booking.html', {'form': form, 'event': event})


