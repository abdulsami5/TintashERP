from django.db import models
from Users.models import *
from project.models import *


class UserProject(models.Model):
    """This model is association class between user and projects"""
    status = models.CharField(max_length=30, blank=True)
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class UserProjectRequest(models.Model):
    """This is model class is to handle requests of employees to be added  or removed from any project"""
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    request_type = models.CharField(max_length =50)
    status = models.CharField(max_length = 50, blank=True)
    reason = models.TextField(max_length = 100, blank=True)
    def save(self, *args, **kwargs):
        """ Function that converts request_type to lower case at the time of saving it in database"""
        self.request_type = self.request_type.lower()
        self.status = self.status.lower()
        return super(UserProjectRequest, self).save(*args, **kwargs)
