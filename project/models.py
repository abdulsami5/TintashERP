from django.db import models
from Users.models import *

class Project(models.Model):
    """Project model class"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
