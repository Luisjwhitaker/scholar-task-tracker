from rest_framework import serializers
from slp_logs.models import *

from django.contrib.auth.models import User

class TaskEntrySerializer(serializers.ModelSerializer):
    def getUsername(self, obj):
        return obj.user.username
    username = serializers.SerializerMethodField("getUsername")
    class Meta:
        model = TaskEntry
        fields = ('username', 'user', 'adventure_slp', 'arena_slp', 'quest_slp', 'date_submitted')

#    def create(self, validated_data):
#        user = validated_data['user'],
#        adventure_slp = validated_data['adventure_slp'],
#        arena_slp = validated_data['arena_slp'],
#        quest_slp = validated_data['quest_slp'],

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style=('input_type':'password'), write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password': {'write_only' : True}
        }

    def save(self):
        account = User(
            email=self.validated_data['email']
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
            account.set_password(password)
            accound.save()

        return User
