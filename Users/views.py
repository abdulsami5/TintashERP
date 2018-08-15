from django.shortcuts import render
from oauth2_provider.models import Application, AccessToken
from .models import User


def get_user(request):
    """This function is to get user object from request's access-token"""
    token_string = request.META.get("HTTP_AUTHORIZATION")
    if token_string:
        try:
            token_string = token_string.split()
            access_token = AccessToken.objects.get(token=token_string[1])
            user = User.objects.get(id=access_token.user_id)
            return user
        except (AccessToken.DoesNotExist, User.DoesNotExist) as e:
            return None
    else:
        None
