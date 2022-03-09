from tkinter import CASCADE
from django.db import models

# Create your models here.

class Directorate(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=50)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)

    def __str__(self):
        return self.directorate

class Unit(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.department

class SubUnit(models.Model):
    title = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit

class EmploymentDetails(models.Model):
    #biodata = models.ForeignKey(Biodata, on_delete=models.CASCADE)
    ministry = models.CharField(max_length=100)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    #salary_scale = models.ForeignKey(Salary, on_delete=models.CASCADE)
    grade = models.IntegerField(max_length=2)
    step = models.IntegerField(max_length=1)
    ippis_no = models.IntegerField(max_length=6, unique=True)

    def __str__(self):
        return self.ministry

#class LeaveApplication(models.Model):
    #leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    #duration = models.IntegerField(max_length=2)
    #requested_duration = models.IntegerField(max_length=2)
    #date_from = models.DateField
    #date_to = models.DateField
    #date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #status = models.ForeignKey(LeaveAppStatus, on_delete=models.CASCADE, blank=True)

    #def __str__(self):
        #return {self.}