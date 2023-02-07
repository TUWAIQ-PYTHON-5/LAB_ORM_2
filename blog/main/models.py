from django.db import models

# Create your models here.

class Post (models.Model):
   
    Title = models.CharField(max_length=1024)
    Content = models.TextField(blank=True)
    is_published = models.BooleanField(blank=True)
    publish_date =models.DateTimeField()
