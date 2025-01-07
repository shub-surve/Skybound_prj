from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
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
    """
    Render the homepage with the Hero, Destinations, and Training sections.
    """
    
    return render(request, 'home.html')

def get_all_events(request):
    events = Event.objects.all() 
    return render(request, 'events.html', {'events': events})


# Get Event View
def get_event_and_mail(request, id):
    event = get_object_or_404(Event, pk=id)
    mail_sent = False
    if request.method == 'POST':
        form = GetDetailsForm(request.POST, initial={'event': event})
        if form.is_valid():
            form.save()

            # Email Logic
            subject = 'Thank you for contacting SkyBound'
            to_email = form.cleaned_data['email']
            context = {
                'event': event,
                'booking_link': "#",  
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
                mail_sent = True
            except Exception as e:
                print(f"Error sending email: {e}")
                
        else:
            print(f"Form errors: {form.errors}")
    
    form = GetDetailsForm(initial={'event': event})
    
    return render(request, 'event_details.html', {'event': event, 'form': form , 'mail_sent': mail_sent})

        



def user_logout(request):
    logout(request)
    return redirect('home')
