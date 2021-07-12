from rest_framework import serializers
from slp_logs.models import *

class TaskEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEntry
        fields = ['user', 'date_submitted', 'adventure_slp', 'arena_slp', 'quest_slp']
