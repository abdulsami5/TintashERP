from django.core.exceptions import PermissionDenied
from .models import User
from Users.models import User
from project.models import Project
from .views import get_user
from oauth2_provider.models import Application, AccessToken
from rest_framework.response import Response
from rest_framework import status


def has_role(role):
    """This decorator is to check \
    the permission of user access the view function"""
    def decorator(function):
        def wrap(self, request, *args, **kwargs):
            user = get_user(request)
            if user:
                if user.groups.filter(name=role).count()>0:
                    return function(self, request)
                else:
                    raise PermissionDenied
            else:
                return Response({"message : Cant find user"},status=status.HTTP_400_BAD_REQUEST)
        return wrap
    return decorator

def has_role_function(role):
    """This decorator is to check \
    the permission of user access the view function"""
    def decorator(function):
        def wrap(request, *args, **kwargs):
            user = get_user(request)
            if user:
                if user.groups.filter(name=role).count()>0:
                    return function(request)
                else:
                    raise PermissionDenied
            else:
                return Response({"message : Cant find user"},status=status.HTTP_400_BAD_REQUEST)
        return wrap
    return decorator

def is_project_pm(function):
    """This decorator is to check if requesting user \
    is the PM of requested project"""
    def decorator(self, request, *args, **kwargs):
        project_id = request.GET.get('project_id')
        if project_id:
            try:
                user = get_user(request)
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return Response({"message : Some parameters are not correct"},status=status.HTTP_400_BAD_REQUEST)
            if project.manager and user:
                if project.manager.id == user.id:
                    return function(self,request)
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        else:
            return Response({"message : Parameters missing"},status=status.HTTP_400_BAD_REQUEST)
    return decorator


