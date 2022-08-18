from django.db import models

# Create your models here.


class Employee(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=50)
    deptName = models.CharField(max_length=10)
    empAge = models.IntegerField()
