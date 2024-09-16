from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.db import transaction
from .models import Departments, Employees
from .serializers import DepartmentsSerializer, EmployeesSerializer


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        return get_departments()

    elif request.method == "POST":
        return create_or_update_department(request)

    elif request.method == "PUT":
        return update_department(request)

    elif request.method == "DELETE":
        return delete_department(id)

    return HttpResponseBadRequest("متد غیرمجاز")


def get_departments():
    departments = Departments.objects.all()
    serializer = DepartmentsSerializer(departments, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_or_update_department(request):
    department_data = JSONParser().parse(request)
    serializer = DepartmentsSerializer(data=department_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "رکورد با موفقیت اضافه شد"}, status=201)
    return JsonResponse({"error": "اعتبارسنجی ناموفق", "details": serializer.errors}, status=400)


def update_department(request):
    department_data = JSONParser().parse(request)
    try:
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        serializer = DepartmentsSerializer(department, data=department_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "رکورد با موفقیت به‌روزرسانی شد"})
        return JsonResponse({"error": "اعتبارسنجی ناموفق", "details": serializer.errors}, status=400)
    except Departments.DoesNotExist:
        return HttpResponseNotFound("دپارتمان مورد نظر یافت نشد.")


def delete_department(id):
    try:
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse({"message": "رکورد با موفقیت حذف شد"})
    except Departments.DoesNotExist:
        return HttpResponseNotFound("دپارتمان مورد نظر یافت نشد.")


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == "GET":
        return get_employees()

    elif request.method == "POST":
        return create_employee(request)

    elif request.method == "PUT":
        return update_employee(request)

    elif request.method == "DELETE":
        return delete_employee(id)

    return HttpResponseBadRequest("متد غیرمجاز")


def get_employees():
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_employee(request):
    employee_data = JSONParser().parse(request)
    employee_data.pop('EmployeesId', None)  # حذف EmployeesId برای ایجاد رکورد جدید
    serializer = EmployeesSerializer(data=employee_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "رکورد با موفقیت اضافه شد"}, status=201)
    return JsonResponse({"error": "اعتبارسنجی ناموفق", "details": serializer.errors}, status=400)


def update_employee(request):
    employee_data = JSONParser().parse(request)
    try:
        employee = Employees.objects.get(EmployeesId=employee_data['EmployeesId'])
        serializer = EmployeesSerializer(employee, data=employee_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "رکورد با موفقیت به‌روزرسانی شد"})
        return JsonResponse({"error": "اعتبارسنجی ناموفق", "details": serializer.errors}, status=400)
    except Employees.DoesNotExist:
        return HttpResponseNotFound("کارمند مورد نظر یافت نشد.")


def delete_employee(id):
    try:
        employee = Employees.objects.get(EmployeesId=id)
        employee.delete()
        return JsonResponse({"message": "رکورد با موفقیت حذف شد"})
    except Employees.DoesNotExist:
        return HttpResponseNotFound("کارمند مورد نظر یافت نشد.")
