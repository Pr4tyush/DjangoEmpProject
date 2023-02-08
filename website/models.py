from django.db import models

# Create your models here.
class Student(models.Model):                 #WITH THIS I CAN MAKE A COLUMN AT SQL db 
                                             #and then use command py manage.py shell in terminal and then ADD some entries on shell that can reflected on sql database
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    rollno= models.IntegerField(max_length=10)
    isactive = models.BooleanField(default=False)
