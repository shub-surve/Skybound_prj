from django.shortcuts import render , get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from bookings.models import Event_Booking
# Create your views here.

def all_blogs(request):
    blogs = BlogPost.objects.prefetch_related('images').all()
    return render(request , 'blogs.html' , {'blogs' : blogs})

def single_blog(request , id):
    blog = get_object_or_404(BlogPost , pk=id)
    return render(request , 'blog.html' , {'blog' : blog})

def safety_inst(request):
    return render(request , 'basics/safety_inst.html')

@login_required
def profile_view(request):
    user = request.user
    bookings = Event_Booking.objects.filter(user=user).select_related('event')
    context = {
        'user': user,
        'bookings': bookings,
    }
    return render(request, 'profile.html', context)


def faq_page(request):
    return render(request , 'basics/faq.html')