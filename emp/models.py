from django.db import models
from django.conf import settings

# Create your models here.
class Emp(models.Model):

    emp_id = models.CharField(max_length=100, primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_dept = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="emp")
    emp_salary = models.FloatField()
    date_join = models.DateField()
    emp_address = models.TextField()

    def __str__(self) -> str:
        return self.emp_name
    