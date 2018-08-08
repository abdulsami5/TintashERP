from django.urls import path
from . import views 

urlpatterns = [
    path('loghours', views.LogHoursApiView.as_view()),
]
