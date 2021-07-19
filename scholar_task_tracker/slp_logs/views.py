from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def logs_view(request):
    taskentry = TaskEntry.objects.all()
    return render(request,'slp_logs/previous_logs.html',{'taskentry':taskentry})
