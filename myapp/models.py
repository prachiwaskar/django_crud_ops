from django.db import models


# Create your models here.


class MyModel(models.Model):
    STUDENT_NO = models.IntegerField()
    STUDENT_NAME = models.CharField(max_length=30)
    STUDENT_DOB = models.DateField()
    STUDENT_DOJ = models.DateField()

