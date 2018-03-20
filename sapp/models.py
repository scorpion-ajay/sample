from django.db import models
import schedule
# Create your models here.

class user(models.Model):
	username = models.CharField(max_length = 100,blank=False,primary_key=True)
	name = models.CharField(max_length = 100,blank=False)
	contact = models.CharField(max_length=15,blank=False)
	def __str__(self):
		return self.name
	def job(request):
		print("I'm working...")
	def str(self):
		while True:
			schedule.every(1).seconds.do(job)