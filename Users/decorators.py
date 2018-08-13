from django.core.exceptions import PermissionDenied
from .model import User


def has_permission(function):
    """This decorator is to check the permission of user access the view function"""
    pass
