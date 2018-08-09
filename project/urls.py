from django.urls import path
from . import views 

urlpatterns = [
    path('project', views.ProjectApiView.as_view()),
    path('activeprojects', views.get_active_projects, name='activeprojects'),
]
