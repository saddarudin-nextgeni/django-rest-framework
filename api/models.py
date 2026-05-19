from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    about = models.TextField()


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)