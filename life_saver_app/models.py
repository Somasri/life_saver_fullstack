from django.db import models

class Users(models.Model):
  mobile = models.IntegerField()
  bikenum = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=255)