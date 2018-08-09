from django.urls import path, include
from . import views

urlpatterns = [
    path('user_projects',views.user_projects),
    path('employee_project_request',views.employee_project_request),
    path('employee_requests_all',views.employee_requests_all),
    path('request_response', views.request_response),
    path('project_all_requests',views.project_all_requests)
]
