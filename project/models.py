from django.db import models

class Project(models.Model):
    """Project model class"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
