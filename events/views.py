from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.conf import settings
from io import BytesIO
from xhtml2pdf import pisa
from .models import Event, CourseDetails
from .forms import GetDetailsForm


# Function to generate PDF


def generate_pdf(template_name, context):
    """
    Generates a PDF from the provided HTML template and context.
    """
    html_content = render_to_string(template_name, context)
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
    if pisa_status.err:
        return None 
    pdf_buffer.seek(0)
    return pdf_buffer.read()



# Home View
def home(request):
    return render(request, 'home.html')


# List All Events
def get_all_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


# Get Event and Send Mail
def get_event_and_mail(request, id):
    event = get_object_or_404(Event, pk=id)
    mail_sent = False

    if request.method == 'POST':
        form = GetDetailsForm(request.POST)

        if form.is_valid():
            # Save user details
            user_details = form.save(commit=False)
            user_details.event = event
            user_details.save()

            # Generate PDF
            context = {'event': event}
            attach_pdf = generate_pdf('template_mail/sendemail.html', context)

            if attach_pdf is None:
                return render(
                    request,
                    'event_details.html',
                    {
                        'event': event,
                        'form': form,
                        'mail_sent': False,
                        'error': "Error generating PDF.",
                    },
                )

            # Email Logic
            subject = 'Thank you for contacting SkyBound'
            to_email = form.cleaned_data['email']
            html_message = render_to_string('email_template.html', context)

            try:
                email = EmailMessage(
                    subject,
                    html_message,
                    from_email='shubhamsurve30803@gmail.com',
                    to=[to_email],
                )
                email.content_subtype = 'html'
                email.attach('email_details.pdf', attach_pdf, 'application/pdf')
                email.send()
                mail_sent = True
                print("Mail sent:", mail_sent)
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = GetDetailsForm()

    return render(request, 'event_details.html', {'event': event, 'form': form, 'mail_sent': mail_sent})


# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')


# List All Courses
def view_all_course(request):
    courses = CourseDetails.objects.all()
    return render(request, 'course/view_all_course.html', {'courses': courses})


# View Course Details
def view_course(request, pk):
    course = get_object_or_404(CourseDetails.objects.prefetch_related('trainer'), pk=pk)
    return render(request, 'course/course_detail.html', {'course': course})
