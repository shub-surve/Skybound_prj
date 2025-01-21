from django.db import models
from bookings.models import Event_Booking , Course_Booking
from django.contrib.contenttypes.fields import GenericForeignKey

class EventPayment(models.Model):
    booking = models.OneToOneField(Event_Booking, on_delete=models.CASCADE, related_name='payment')
    order_id = models.CharField(max_length=255, unique=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    status = models.CharField(max_length=50, default='Pending')  # Success, Failed, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event Payment - {self.booking.event.name} - {self.status}"

class CoursePayment(models.Model):
    booking = models.OneToOneField(Course_Booking, on_delete=models.CASCADE, related_name='payment')
    order_id = models.CharField(max_length=255, unique=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    status = models.CharField(max_length=50, default='Pending')  # Success, Failed, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event Payment - {self.booking.event.name} - {self.status}"
