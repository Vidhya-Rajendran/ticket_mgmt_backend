from django.db import models
from django.utils import timezone
import random
import string

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True) # True = available, False = on leave

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.emp_id:
            super().save(*args, **kwargs)
            self.emp_id = f"EMP-{self.id}"  # eg. EMP-1
        return super().save(*args, **kwargs)


class EmployeeDutyRoster(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, related_name='roster')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    ticket = models.ManyToManyField('tickets.Ticket', related_name="+", blank=True)
    is_employee_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"