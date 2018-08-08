from django.urls import path, include
from . import views

urlpatterns = [
    path('user_projects',views.user_projects),
    path('employee_project_request',views.employee_project_request),
    path('employee_requests_all',views.employee_requests_all),
    path('accept_request',views.accept_request),
]
