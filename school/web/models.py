from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, unique=True, default=1)
    is_present = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)