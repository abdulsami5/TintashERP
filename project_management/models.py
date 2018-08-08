from django.db import models
from Users.models import *
from project.models import *


class UserProject(models.Model):
    """This model is association class between user and projects"""
    status = models.CharField(max_length=30, blank=True)
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
