from EmployeeApp.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('empId', 'empName', 'deptName', 'empAge')
