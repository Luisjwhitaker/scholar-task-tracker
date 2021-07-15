from django.urls import path,include
from . import views
from account import views as account_views
#urlpatterns = []
urlpatterns = [
    path('', views.logs_view),
    path('register/', account_views.register),
    # REST FRAMEWORK URLS
    path('api/task/<str:primery_key>', include('slp_logs.api.urls','task-tracker-api')),
]
