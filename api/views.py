from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializer import CompanySerializer, EmployeeSerializer

# viewsets provide the implementation for CRUD operations by default
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer