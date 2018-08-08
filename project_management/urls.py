from django.urls import path, include
from . import views

urlpatterns = [
    path('user_projects',views.user_projects),
]
