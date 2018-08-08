from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
@csrf_exempt
@api_view(['GET',])
def user_projects(request):
    """This method or api function will return all projects of employee, given employee_id as parameter"""
    user_id = request.GET.get('user_id')
    user_projects = UserProject.objects.filter(employee=user_id)
    user_projects_serializer = UserProjectSerializer(user_projects, many=True)
    return Response({"user_projects":user_projects_serializer.data},status=status.HTTP_200_OK)
