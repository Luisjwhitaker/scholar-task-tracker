from rest_framework import serializers
from slp_logs.models import *

class TaskEntrySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = TaskEntry
        fields = ['user', 'adventure_slp', 'arena_slp', 'quest_slp', 'date_submitted']
