from django.urls import path
from .views import event_booking_view , course_booking_view

urlpatterns = [
    path('event-booking/<int:id>/', event_booking_view, name='event_booking'),
    path('course-booking/<int:id>/' , course_booking_view , name='course_booking')
]
