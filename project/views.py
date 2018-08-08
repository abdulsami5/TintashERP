from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer
from .models import Project

class ProjectApiView(APIView):
    """Project APIview to handle all restfull requests"""
    def get(self,request, format=None):
        """This method will return either all projects or a signle proect if passed project_id as parameter"""
        project_id = request.GET.get('project_id')
        if project_id:
            project = Project.objects.filter(id=project_id)
            if project:
                project_serializer = ProjectSerializer(project, many=True)
            else:
                return Response({"message":"No record found"},status = status.HTTP_404_NOT_FOUND)
        else:
            projects = Project.objects.all()
            project_serializer = ProjectSerializer(projects, many=True)
        return Response({"data":project_serializer.data})
