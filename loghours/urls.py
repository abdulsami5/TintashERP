from django.urls import path
from . import views 

urlpatterns = [
    path('loghours', views.LogHoursApiView.as_view()),
    path('projectloghours', views.ProjectLogHourApiView.as_view()),
    path('unapprovedhour', views.get_unapproved_hours),
]
