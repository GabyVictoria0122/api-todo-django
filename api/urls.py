from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks>', views.api_tasks, name="tasks"),
    path('api/user>', views.api_user, name="user"),
]
