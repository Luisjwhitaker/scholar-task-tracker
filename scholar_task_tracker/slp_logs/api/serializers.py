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
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2',]
        extra_kwargs = {
            'password':{'write_only':True},
            'std_code': {'required': False},
            'uni_code': {'required': False},
            'last_name': {'required': False},
            'first_name': {'required': False}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user

#    def save(self):
#        account = User(
#            email=self.validated_data['email']
#            username=self.validated_data['username']
#        )
#        password = self.validated_data['password']
#        password2 = self.validated_data['password2']
#
#        if password != password2:
#            raise serializers.ValidationError({'password':'Passwords must match.'})
#            account.set_password(password)
#            accound.save()
#
#        return User
