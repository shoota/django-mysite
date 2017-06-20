from django.db import models
from django.utils import timezone

class ClubTeam(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100, null=True)
	created_date = models.DateTimeField(default=timezone.now) 

	def __str__(self):
		return self.name