from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=300)

    def __str__(self):
        return self.DepartmentName

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=500)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    DateOfBirth = models.DateTimeField()
    PhotoFileName = models.CharField(max_length=500)

    def __str__(self):
        return self.EmployeesName
