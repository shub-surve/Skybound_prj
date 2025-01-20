from django.shortcuts import render , get_object_or_404
from .forms import Event_Booking_Form
from .models import Event_Booking
from events.models import Event
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .forms import Event_Booking_Form
from .models import Event

def event_booking_view(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == 'POST':
        form = Event_Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            print(booking)
    else:
        form = Event_Booking_Form()
    return render(request, 'event_booking.html', {'form': form, 'event': event})

