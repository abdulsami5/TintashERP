from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(User):
    """This is the User model for database"""
    profile_pic = models.CharField(blank=True, max_length=1000)
    contact_info = models.CharField(blank=True, max_length=30)


    def __str__(self):
        """This function is to get representation of User model"""
        return self.email
