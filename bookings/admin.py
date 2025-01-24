from django.contrib import admin
from .models import Event_Booking , Course_Booking
# Register your models here.

admin.site.register([Event_Booking , Course_Booking])