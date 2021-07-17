from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=150, default='no nickname')
	manager_percent = models.PositiveSmallIntegerField(default=0)
	investor_percent = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return f"{self.user.username}'s Profile"
