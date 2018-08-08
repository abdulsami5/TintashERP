from rest_framework import serializers
from .models import *

class UserProjectSerializer(serializers.ModelSerializer):
    """This is the serializer class for UserProject"""
    class Meta:
        """Meta class for UserProject"""
        model = UserProject
        fields = ('status', 'employee','project','id')
