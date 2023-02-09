from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=1024)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add=True)