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
    phone_no = models.CharField(max_length=20, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)  # ForeignKey to Event model

class Trainers(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(upload_to='trainers'  , default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    no_of_jumps = models.PositiveIntegerField()

class CourseDetails(models.Model):
    course_name = models.CharField(max_length=50)
    course_duration = models.CharField(max_length=50)
    start_date = models.DateField()
    course_desc = RichTextField()
    itinerary = RichTextField()
    whats_included = RichTextField()
    whats_not_included = RichTextField()
    trainer = models.ManyToManyField(Trainers , null=True , blank=True)

    def __str__(self):
        return super().__str__()

class Course_image(models.Model):
    course = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    models.ImageField(upload_to='course', height_field=None, width_field=None, max_length=None)

class CourseLevel(models.Model):
    course = models.OneToOneField(CourseDetails, on_delete=models.CASCADE)
    level = models.IntegerField()
    level_desc = RichTextField()

