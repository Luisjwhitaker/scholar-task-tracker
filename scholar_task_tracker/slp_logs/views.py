from django.shortcuts import render
from .models import *

# Create your views here.

def logs_view(request):
    taskentry = TaskEntry.objects.all()
    return render(request,'slp_logs/previous_logs.html',{'taskentry':taskentry})
