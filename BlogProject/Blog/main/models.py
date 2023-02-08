from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
 


    