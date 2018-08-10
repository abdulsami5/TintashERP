Xfrom django.urls import path
from . import views 

urlpatterns = [
    path('loghours', views.LogHoursApiView.as_view()),
    path('projectloghours', views.ProjectLogHourApiView.as_view())
]
