from django.db import models

class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
