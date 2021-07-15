from django.db import models
from django.contrib.auth.models import User
from account.models import *
# Create your models here.
class TaskEntry(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    adventure_slp = models.PositiveSmallIntegerField(default=0)#,max_value=100)
    arena_slp = models.PositiveSmallIntegerField(default=0)#,max_value=500)
    quest_slp = models.PositiveSmallIntegerField(default=0)#,max_value=50)

    def __str__(self):
        return f'{self.user} - {self.date_submitted.strftime("%b %d %Y - %H:%M")}'

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s profile"
