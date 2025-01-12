from django.contrib import admin
from .models import Event, UserDetails, Trainers, CourseDetails, Course_image, CourseLevel

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'package', 'capacity', 'registration_amt', 'price_details', 'created_at', 'updated_at')
    search_fields = ('name', 'package')
    list_filter = ('created_at', 'updated_at')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_no', 'event')
    search_fields = ('username', 'email')
    list_filter = ('event',)

class TrainersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'desc', 'no_of_jumps')
    search_fields = ('first_name', 'last_name')
    list_filter = ('no_of_jumps',)

class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_duration', 'start_date')
    search_fields = ('course_name',)
    list_filter = ('start_date',)

class CourseImageAdmin(admin.ModelAdmin):
    list_display = ('course',)
    search_fields = ('course',)
    list_filter = ('course',)

class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('course', 'level')
    search_fields = ('course',)
    list_filter = ('level',)

admin.site.register(Event, EventAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(Trainers, TrainersAdmin)
admin.site.register(CourseDetails, CourseDetailsAdmin)
admin.site.register(Course_image, CourseImageAdmin)
admin.site.register(CourseLevel, CourseLevelAdmin)
