from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer
from .models import Project
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q
import datetime
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from Users.decorators import has_role, is_project_pm, has_role_function



class ProjectApiView(APIView):
    """Project APIview to handle all restfull requests"""
    @has_role("Employee")
    def get(self,request, format=None):
        """This method will return either all projects or a single project if passed project_id as parameter"""
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

    @has_role("Financial Controller")
    def post(self,request, format=None):
      """This method will crete a new project object """
      project_serializer = ProjectSerializer(data=request.data)
      if project_serializer.is_valid():
        project_serializer.save()
        return Response({"message":"Project created successfully"},status = status.HTTP_201_CREATED)
      else:
          return Response({"message":project_serializer.errors},status = status.HTTP_403_FORBIDDEN)

    @has_role("Financial Controller")
    def put(self,request,format=None):
        """This method will be used to update project"""
        try:
            project_id = request.data.get("id")
            project = Project.objects.get(id=project_id)
            project_serializer = ProjectSerializer(project, data=request.data)
            if project_serializer.is_valid():
                project_serializer.save()
                return Response(project_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(project_serializer.errors)
        except Project.DoesNotExist:
            return Response({"message : Bad Request"},status=status.HTTP_400_BAD_REQUEST)

    @has_role("Financial Controller")
    def delete(self,request,format=None):
        """This method will be used to delete a particular project"""
        try:
            project_id = request.data.get("id")
            project = Project.objects.get(id=project_id)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message : Bad Request"},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET',])
@has_role_function("Financial Controller")
def get_active_projects(request):
    """This method is to to get all the projects that are currently active"""
    today = datetime.datetime.today()
    projects = Project.objects.filter(Q(end_date__gte=today)|Q(end_date=None))
    project_serializer = ProjectSerializer(projects, many=True)
    return Response({"data":project_serializer.data})
