from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import timezone

class CustomUser(AbstractUser):
    pass
# Create your models here.
class VideoTutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    youtube_link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='my_pics')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='my_pics')
    link = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title