from django.db import models

# Create your models here.


class empmanage(models.Model):
    name = models.CharField(max_length=200)
    empid = models.IntegerField(max_length=20)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)
