from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    adventure_slp = models.IntegerField(default=0)
    arena_slp = models.IntegerField(default=0)
    quest_slp = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user} - {self.date_submitted.strftime("%b %d %Y - %H:%M")}'

class Scholar(models.Model):
    manager_percent = models.IntegerField(default=0)
    investor_percent = models.IntegerField(default=0)
