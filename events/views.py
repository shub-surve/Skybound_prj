from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event , CourseDetails
from .forms import GetDetailsForm 
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
import os
from django.conf import settings

# Home View
def home(request):
    
    
    return render(request, 'home.html')



def get_all_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def get_event_and_mail(request, id):
    event = get_object_or_404(Event, pk=id)
    mail_sent = False  # Initialize mail_sent variable

    if request.method == 'POST':
        form = GetDetailsForm(request.POST)
        
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.event = event  # Associate the event with the user_details
            user_details.save()

            # Email Logic
            subject = 'Thank you for contacting SkyBound'
            to_email = form.cleaned_data['email']
            context = {
                'event': event,
                'booking_link': "#",  # Replace with the actual booking link
                'support_email': 'support@example.com',
            }
            html_message = render_to_string('email_template.html', context)

            try:
                email = EmailMessage(
                    subject,
                    html_message,
                    from_email='shubhamsurve30803@gmail.com',
                    to=[to_email],
                )
                email.content_subtype = 'html'
                email.send()
                mail_sent = True  # Set mail_sent to True when email is successfully sent
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = GetDetailsForm()  # Initialize the form for GET requests

    return render(request, 'event_details.html', {'event': event, 'form': form, 'mail_sent': mail_sent})



        



def user_logout(request):
    logout(request)
    return redirect('home')




# Course Views
def view_all_course(request):
    courses = CourseDetails.objects.all()
    return render(request , 'course/view_all_course.html' , {'courses' : courses})