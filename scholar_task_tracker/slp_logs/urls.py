from django.urls import path,include
from . import views

#urlpatterns = []
urlpatterns = [
    path('', views.logs_view),
    # REST FRAMEWORK URLS
    path('api/task/<str:primery_key>', include('slp_logs.api.urls','task-tracker-api')),
]
