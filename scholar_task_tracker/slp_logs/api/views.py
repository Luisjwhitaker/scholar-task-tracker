from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from slp_logs.models import TaskEntry
from slp_logs.api.serializers import TaskEntrySerializer

@api_view(['GET',])
def api_task_entry(request,primery_key):
    try:
        taskentry = TaskEntry.objects.get(id=primery_key)
    except TaskEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskEntrySerializer(taskentry)
        return Response(serializer.data)
