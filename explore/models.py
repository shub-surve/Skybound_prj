from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class BlogPost():
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_desc = RichTextField()
    accept = models.BooleanField(default=False)

class BlogImages():
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='Blog_images', height_field=None, width_field=None, max_length=None)


    