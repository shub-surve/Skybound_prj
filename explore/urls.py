from django.urls import path
from .views import *

urlpatterns = [
    path('' , all_blogs , name='blogs' ),
    path('blog/<int:id>' , single_blog , name='blog'),
    path('safety-inst/' , safety_inst , name='safety')
]
