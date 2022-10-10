from pickle import TRUE
from django.db import models
from django.conf import settings
from django.forms import CharField

# Create your models here.

class Dept(models.Model):
    Departments= (
        ('1','IT'),
        ('2','Accounts'),
        ('3','HR'),
        ('4','Procurement'),
    )
    # id = models.CharField(max_length=100, primary_key=True)
    emp_dept = models.CharField(max_length=1, choices=Departments)

class Emp(models.Model):
    # emp_id = models.CharField(max_length=100, primary_key=True)
    emp_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, null=True)
    emp_salary = models.FloatField()
    date_join = models.DateField()
    emp_address = models.TextField()

    def __str__(self) -> str:
        return self.emp_name

class Status(models.Model):
    Statuses = (
        ('1','active'),
        ('2','inactive'),
    )
    intial = models.Field(unique=True)
    status = models.CharField(max_length=1, choices=Statuses)

