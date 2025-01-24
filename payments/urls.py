from django.urls import path
from .views import event_payment_view, course_payment_view, payment_callback

app_name = 'payments'

urlpatterns = [
    path('course-payment/<int:booking_id>', course_payment_view, name='course_payment'),
    path('event-payment/<int:booking_id>', event_payment_view, name='event_payment'),
    path('callback/', payment_callback, name='payment_callback'),
]
