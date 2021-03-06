from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from slp_logs.models import TaskEntry
from slp_logs.api.serializers import TaskEntrySerializer,RegisterSerializer

@api_view(['POST',])
def api_register(request):
    serializer = RegisterSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        user= serializer.save()
        data['responce']= 'successfully registered new user'
        data['username']= user.username
        token = Token.objects.get(user=user).key
        data['token']= token
    else:
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data)

@api_view(['GET',])
def api_overview(request):
    api_urls = {
        'Register':'/register/',
        'Log In':'/login/',
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET',])
def api_task(request):
    try:
        taskentry = TaskEntry.objects.all()
    except TaskEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskEntrySerializer(taskentry, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_task_detail(request,pk):
    try:
        taskentry = TaskEntry.objects.get(id=pk)
    except TaskEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskEntrySerializer(taskentry)
        return Response(serializer.data)

@api_view(['POST',])
def api_task_create(request):
    if request.method == 'POST':
        serializer = TaskEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def api_task_update(request,pk):
    try:
        taskentry = TaskEntry.objects.get(id=pk)
    except TaskEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = TaskEntrySerializer(instance=taskentry , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_task_delete(request,pk):
    try:
        taskentry = TaskEntry.objects.get(id=pk)
        taskentry.delete()
    except TaskEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response('Item Deleted')
