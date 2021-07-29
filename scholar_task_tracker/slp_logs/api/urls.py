from django.urls import path
from . import views

app_name = 'scholar_tast_tracker'

urlpatterns = [
    path('', views.apiOverview, name='api overview'),
    path('task-list/', views.api_task, name='api task list'),
    path('task-detail/<str:pk>/', views.api_task_detail, name='api task detail'),
    path('task-create/', views.api_task_create, name='api task create'),
    path('task-update/<str:pk>/', views.api_task_update, name='api task update'),
    path('task-delete/<str:pk>/', views.api_task_delete, name='api task delete'),
]
