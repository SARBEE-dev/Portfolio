from django.contrib import admin
from .models import VideoTutorial, Certificate, CustomUser, Project

# Register your models here.
admin.site.register(VideoTutorial)
admin.site.register(Certificate)
admin.site.register(CustomUser)
admin.site.register(Project)