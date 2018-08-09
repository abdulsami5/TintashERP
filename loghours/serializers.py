from rest_framework import serializers
from .models import Loghours,ProjectLogHour


class LogHoursSerializer(serializers.ModelSerializer):
    """Serializer class for LogHours model"""
    class Meta:
        """Meta class to define model and fields to serialize"""
        model = Loghours
        fields = ('id','hours_logged','required_hours','pm_approval','am_approval','hourly_rate','is_valid','employee','project_log_hour',)

class ProjectLogHourSerializer(serializers.ModelSerializer):
    """Serializer class for ProjectLogHour model"""
    class Meta:
        """Meta class to define model and fileds to serializer"""
        model = ProjectLogHour
        fields = ("id", "pm_approval", "am_approval", "project")
