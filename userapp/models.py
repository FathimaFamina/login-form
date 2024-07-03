from django.db import models

# Create your models here.

class details(models.Model):
    username = models.CharField(max_length=20,null=True)
    firstname = models.CharField(max_length=20,null=True)
    lastname = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    passwordconfirmation = models.CharField(max_length=20,null=True)

