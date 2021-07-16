from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def register(request):
    form = UserCreationForm()
    return render(request,'account/register.html',{'form':form})

def login(request):
    return render(request,'account/login.html')

@login_required
def profile(request):
    return render(request,'account/profile.html')
