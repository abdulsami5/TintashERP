from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer class for project model"""
    class Meta:
        """ Meta class to define model and fields to serialize"""
        model = Project
        fields = ('id','title','description','start_date','end_date')

