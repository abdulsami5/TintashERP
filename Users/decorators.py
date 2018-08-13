from django.core.exceptions import PermissionDenied
from .models import User
from Users.models import User
from oauth2_provider.models import Application, AccessToken


def has_role(role):
    """This decorator is to check the permission of user access the view function"""
    def decorator(function):
        def wrap(self, request, *args, **kwargs):

            token_string = request.META.get('HTTP_AUTHORIZATION')
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
