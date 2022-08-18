from django.views.decorators.csrf import csrf_exempt
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.


@csrf_exempt
def EmployeeView(request, id=0):
    if request.method == 'GET':
        emp = Employee.objects.all()
        emp_data = EmployeeSerializer(emp, many=True)
        return JsonResponse(emp_data.data, safe=False)

    elif request.method == 'POST':
        emp = JSONParser().parse(request)
        emp_data = EmployeeSerializer(data=emp)
        if emp_data.is_valid():
            emp_data.save()
            return JsonResponse('Successfully Added!', safe=False)
        return JsonResponse('Failed to Added!', safe=False)

    elif request.method == 'PUT':
        emp = JSONParser().parse(request)
        emp_data = Employee.objects.all(empId=emp_data['empId'])
        emp_serializer = EmployeeSerializer(emp_data, data=emp)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return JsonResponse('Successfully Updated!', safe=False)
        return JsonResponse('Failed to Update!', safe=False)

    elif request.method == 'DELETE':
        emp = Employee.objects.get(empId=id)
        emp.delete()
        return JsonResponse("Delete Successfully", safe=False)
