from typing_extensions import TypeGuard
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: 9999999999")

class Student(models.Model):
    """
    This model will store the
    students information
    """
    name = models.CharField(max_length= 100, blank= True, null= True)
    mobile = models.CharField(max_length= 15,unique=True, validators=[phone_regex])
    email = models.EmailField(unique= True)
    city = models.CharField(max_length= 20, blank= True, null= True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    """
    This model will store the
    Teachers information
    """
    name = models.CharField(max_length= 100, blank= True, null= True)
    mobile = models.CharField(max_length= 15, unique=True, validators=[phone_regex])
    email = models.EmailField(unique= True)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    """
    This models will
    store lecture's information
    which have one teacher and multiple students
    """
    name =  models.CharField(max_length= 100, blank= True, null= True)
    description = models.TextField(max_length= 500, blank= True, null= True)
    time = models.DateTimeField(blank= True, null= True)
    teacher = models.ForeignKey(Teacher, on_delete= models.PROTECT, blank= True, null=True)
    student = models.ManyToManyField(Student, blank= True, null= True)

    def __str__(self):
        return self.name