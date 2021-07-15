from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your views here.

def register(request):
    form = UserCreationForm()
    return render(request,'slp_logs/register.html',{'form':form})
