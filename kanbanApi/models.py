from django.db import models


# Create your models here.
class Project(models.Model):
    projectName = models.CharField(max_length=120)
    projectIdentifier = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
