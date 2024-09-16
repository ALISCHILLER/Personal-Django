from rest_framework import serializers
from .models import Departments, Employees

from rest_framework import serializers
from .models import Employees, Departments


class EmployeesSerializer(serializers.ModelSerializer):
    # استفاده از فیلد ForeignKey به عنوان PrimaryKeyRelatedField
    Department_id = serializers.PrimaryKeyRelatedField(
        source='Department',
        queryset=Departments.objects.all(),
        write_only=True
    )

    class Meta:
        model = Employees
        fields = ['EmployeesId', 'EmployeesName', 'Department_id', 'DateOfBirth', 'PhotoFileName']
        # فیلد Department_id را اضافه کنید تا به درستی پردازش شود


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        depth = 1  # مشابه بالا، این گزینه به رابطه‌های تو در تو کمک می‌کند.
