from django.urls import path
from . import views

app_name = 'scholar_tast_tracker'

urlpatterns = [
    path('', views.api_task_entry, name='api task page'),
]
