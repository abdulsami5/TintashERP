from django.db import models
from Users.models import User
from project.models import Project


class ProjectLogHour(models.Model):
    """Model to represent the weekly loghours for a project"""
    date = models.DateField(null=True, blank=True)
    pm_approval = models.BooleanField()
    am_approval = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Loghours(models.Model):
    """ Loghours model class"""
    date = models.DateField(null=True, blank=True)
    hours_logged = models.FloatField(null=True)
    required_hours = models.FloatField(null=True)
    pm_approval = models.BooleanField()
    am_approval = models.BooleanField()
    hourly_rate = models.FloatField(null=True)
    is_valid = models.BooleanField()
    employee = models.ForeignKey(User,blank=True,on_delete=models.DO_NOTHING)
    project_loghour = models.ForeignKey(ProjectLogHour,on_delete=models.CASCADE, null=True)
