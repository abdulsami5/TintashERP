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

@csrf_exempt
@api_view(['POST',])
def employee_project_request (request):
    """This method or api function will create a user request to be added or removed from a particular project"""
    user_project_request_serializer = UserProjectRequestSerializer(data=request.data)
    if user_project_request_serializer.is_valid():
        user_project_request_serializer.save()
        return Response({"message":"Request added successfully"},status = status.HTTP_201_CREATED)
    else:
        return Response({"message":user_project_request_serializer.errors},status = status.HTTP_403_FORBIDDEN)

@csrf_exempt
@api_view(['GET',])
def employee_requests_all(request):
    """This method or api function will return all user_requets of employee, given employee_id as parameter"""
    user_id = request.GET.get('user_id')
    user_requests = UserProjectRequest.objects.filter(employee=user_id)
    user_project_request_serializer = UserProjectRequestSerializer(user_requests, many=True)
    return Response({"user_requests":user_project_request_serializer.data},status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def request_response(request):
    """ This method or api is for pm to accept request for employees to be added to project"""
    data = request.data
    request_id = data.get("request_id")
    request_response = data.get("response","none")
    print(request_response)
    try:
        user_project_request = UserProjectRequest.objects.get(id=request_id)
        if request_response.lower() == 'accept':
            user_project_request.status = "accepted"
            user_project_request.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif  request_response.lower() == 'reject':
            user_project_request.status = "rejected"
            user_project_request.reason = data.get("reason", "No reason stated.")
            user_project_request.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "correct parameters not found or parameter missing"},status=status.HTTP_400_BAD_REQUEST)
    except UserProjectRequest.DoesNotExist:
        return Response({"message": "Record not found"},status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
def project_all_requests(request):
    """This api end point will return all pending requests for a project that are yet to be approved or rejected, taking project_id as input"""
    data = request.data
    project_id = data["project_id"] #Make it get and put in try catch
    user_project_requests = UserProjectRequest.objects.filter(id=project_id,status='')
    user_project_request_serializer = UserProjectRequestSerializer(user_project_requests, many=True)
    if user_project_request_serializer.data:
        return Response({"Requests":user_project_request_serializer.data},status=status.HTTP_200_OK)
    return Response({"message": "Record not found"},status=status.HTTP_404_NOT_FOUND)
