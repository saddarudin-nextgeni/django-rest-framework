from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializer import CompanySerializer, EmployeeSerializer

# viewsets provide the implementation for CRUD operations by default
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = self.get_object()
        employees = company.employees.all()
        serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer