from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
        else:
            messages.error(request, f'error')
    else:
        form = UserRegisterForm()
    return render(request,'account/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'account/profile.html')
