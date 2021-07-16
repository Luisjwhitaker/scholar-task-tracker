from django.urls import path,include
from . import views
from account import views as account_views
#urlpatterns = []
urlpatterns = [
    path('previous_logs', views.logs_view, name='previous logs'),
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login, name='login'),
    path('profile/', account_views.profile, name='profile'),
    #path('lobby/', views.lobby, name='lobby'),

    # REST FRAMEWORK URLS
    path('api/task/<str:primery_key>', include('slp_logs.api.urls','task-tracker-api')),
]
