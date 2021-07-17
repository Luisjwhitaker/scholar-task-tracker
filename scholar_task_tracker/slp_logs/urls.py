from django.urls import path,include
from django.contrib.auth import views as auth_views
from account import views as account_views
from . import views
#urlpatterns = []
urlpatterns = [
    path('', views.logs_view, name='home'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/login.html'), name='logout'),
    path('profile/', account_views.profile, name='profile'),
    #path('lobby/', views.lobby, name='lobby'),

    # REST FRAMEWORK URLS
    path('api/task/<str:primery_key>', include('slp_logs.api.urls','task-tracker-api')),
]
