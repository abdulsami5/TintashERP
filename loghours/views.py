from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loghours
from .serializers import LogHoursSerializer

class LogHoursApiView(APIView):
    """ApiView for loghours"""
    def get(self,request, format=None):
        """This method will return logohours of an employee given user_id and project_id as parameter"""
        project_id = request.GET.get('project_id')
        user_id = request.GET.get('user_id')
        if project_id and user_id:
            logohours = Loghours.objects.filter(project=project_id, employee_id=user_id)
            if logohours:
                loghours_serializer = LogHoursSerializer(logohours, many=True)
            else:
                return Response({"message":"No record found"},status = status.HTTP_404_NOT_FOUND)
        elif project_id:
            logohours = Loghours.objects.filter(project=project_id)
            if logohours:
                loghours_serializer = LogHoursSerializer(logohours, many=True)
            else:
                return Response({"message":"No record found"},status = status.HTTP_404_NOT_FOUND)
        else:
            logohours = Loghours.objects.all()
            loghours_serializer = LogHoursSerializer(logohours, many=True)
        return Response({"data":loghours_serializer.data})

