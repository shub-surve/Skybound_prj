from django.db import models
from events.models import Event , CourseDetails
from django_countries.fields import CountryField
# Create your models here.
EXPERIENCE_CHOICE = [
    ('BEG' , "BEGINNER (with less then 3 jumps)"),
    ('INT' , "INTERMIDIATE (with more the 5 jumps less then 10)"),
    ('ADV' , 'ADVANCE (with AFF or WSJC certifications)')
]

EMERGENCY_RELATION = [
    ('MOTHER' , 'MOTHER'),
    ('FATHER' , 'FATHER'),
    ('BROTHER' , 'BROTHER'),
    ('SISTER' , 'SISTER'),
    ('FRIEND' , 'FRIEND'),
    ('OTHERS' , 'OTHERS'),
]

class Event_Booking(models.Model):
    """
    Events Booking-routes to payment
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.PositiveSmallIntegerField()
    height = models.FloatField()
    country = CountryField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    experience = models.CharField(choices=EXPERIENCE_CHOICE, max_length=50)
    special_req = models.CharField(max_length=254 , blank=True , null=True)
    emergency_contact_person_name = models.CharField(max_length=100)
    emergency_contact_person_relation = models.CharField(choices=EMERGENCY_RELATION ,max_length=50)
    emergency_contact_person_number = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default="Pending") 
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event.name}"
    

class Course_Booking(models.Model):
    """
    Course Booking-routes to payment
    """
    course = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.PositiveSmallIntegerField()
    height = models.FloatField()
    country = CountryField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    experience = models.CharField(choices=EXPERIENCE_CHOICE, max_length=50)
    special_req = models.CharField(max_length=254 , blank=True , null=True)
    emergency_contact_person_name = models.CharField(max_length=100)
    emergency_contact_person_relation = models.CharField(choices=EMERGENCY_RELATION ,max_length=50)
    emergency_contact_person_number = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default="Pending") 
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course.name}"
    


    



    

