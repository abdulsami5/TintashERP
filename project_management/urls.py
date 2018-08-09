from django.urls import path, include
from . import views

urlpatterns = [
    path('user_projects',views.user_projects),
    path('employee_project_request',views.employee_project_request),
    path('employee_requests_all',views.employee_requests_all),
    path('request_response', views.request_response),
    path('all_pending_project_requests',views.all_pending_project_requests)
]
