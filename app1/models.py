from django.db import models




# Create your models here.
class Student(models.Model):
    NAME=models.CharField(max_length=30)
    PHONE=models.IntegerField()
    EMAIL=models.EmailField()
    SNAME=models.CharField(max_length=30)
    MSG=models.CharField(max_length=100)

class Contact(models.Model):
    NAME = models.CharField(max_length=30)
    PHONE = models.IntegerField()
    EMAIL = models.EmailField()
    MSG = models.CharField(max_length=100)    