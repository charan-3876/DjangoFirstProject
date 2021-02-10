from django.db import models
from datetime import date
from django.contrib.auth.models import User 
# Create your models here.
class NewJobs(models.Model):

   SerialNumber = models.IntegerField()
   company = models.CharField(max_length=255)
   title = models.CharField(max_length=255)
   location = models.CharField(max_length=255)
   postdate = models.DateTimeField(blank=True)
   lastdate = models.DateTimeField(blank=True)
   action = models.CharField(max_length=255)
   
   def __str__(self):
      return self.title

