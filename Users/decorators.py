from django.core.exceptions import PermissionDenied
from .models import User
from Users.models import User
from project.models import Project
from oauth2_provider.models import Application, AccessToken
from rest_framework.response import Response
from rest_framework import status


def has_role(role):
    """This decorator is to check \
    the permission of user access the view function"""
    def decorator(function):
        def wrap(self, request, *args, **kwargs):
            token_string = request.META.get('HTTP_AUTHORIZATION')
            print(token_string)
            if token_string:
                token_string = token_string.split()
                access_token = AccessToken.objects.get(token=token_string[1])
                user = User.objects.get(id=access_token.user_id)
                print(user.groups.filter(name=role).count())
                if access_token and user.groups.filter(name=role).count()>0:
                    return function(self, request)
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        return wrap
    return decorator


def is_project_pm(function):
    """This decorator is to check if requesting user \
    is the PM of requested project"""
    def decorator(self, request, *args, **kwargs):
        token_string = request.META.get('HTTP_AUTHORIZATION')
        project_id = request.GET.get('project_id')
        if token_string and project_id:
            token_string = token_string.split()
            try:
                access_token = AccessToken.objects.get(token=token_string[1])
                user = User.objects.get(id=access_token.user_id)
                project = Project.objects.get(id=project_id)
            except:
                return Response({"message : Some parameters are not correct"},status=status.HTTP_400_BAD_REQUEST)
            if project.manager:
                if project.manager.id == user.id:
                    return function(self,request)
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        else:
            return Response({"message : Parameters missing"},status=status.HTTP_400_BAD_REQUEST)
    return decorator


