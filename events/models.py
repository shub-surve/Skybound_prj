from django.db import models
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()  # General description
    package = models.CharField(max_length=100)
    capacity = models.IntegerField()
    registration_amt = models.DecimalField(max_digits=10, decimal_places=2)
    price_details = models.DecimalField(max_digits=10, decimal_places=2)
    whats_included = RichTextField(blank=True, null=True)  # New field for inclusions
    whats_not_included = RichTextField(blank=True, null=True)  # New field for exclusions
    itinerary = RichTextField(blank=True, null=True)  # New field for itinerary
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_img = models.ImageField(upload_to='event/covers', max_length=None)

class UserDetails(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20 , blank=True)
    # event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to Event model