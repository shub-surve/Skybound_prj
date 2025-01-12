from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import get_event_and_mail, home, get_all_events , view_all_course , view_course

urlpatterns = [
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('event/', get_all_events, name='events_page'),
    path('event_details/<int:id>', get_event_and_mail, name='event_details'),
    path("course/",view_all_course, name="courses"),
    path("course-detail/<int:pk>", view_course , name='course_detail' )

]