from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1500)
    text = models.TextField()
    date_added = models.DateField(auto_now=True, blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=False)

    def __str__(self):
        return self.title
