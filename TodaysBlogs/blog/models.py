from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=1024)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateField()



