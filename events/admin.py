from django.contrib import admin
from .models import Event , UserDetails , CourseDetails , CourseLevel , Trainers
# Register your models here.
admin.site.register([Event , UserDetails ,CourseLevel , CourseDetails ])
