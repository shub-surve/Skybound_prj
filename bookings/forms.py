from django import forms
from .models import Event_Booking


class Event_Booking_Form(forms.ModelForm):
    class Meta:
        model = Event_Booking
        fields = ['first_name' , 'last_name' , 'email' , 'age' , 'height' , 'country' , 'state' , 'city' , 'experience' , 'special_req' , 'emergency_contact_person_name' , 'emergency_contact_person_relation' ,'emergency_contact_person_number' ]
