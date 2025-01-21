from django.urls import path
from .views import event_booking_view

urlpatterns = [
    path('event-booking/<int:id>/', event_booking_view, name='event_booking'),
]
