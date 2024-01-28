from django.db import models

# Create your models here.
class STUDENTS(models.Model):
    s_reg=models.CharField(max_length=15)
    s_name=models.CharField(max_length=15)
    s_email=models.CharField(max_length=30)
    s_department=models.CharField(max_length=15)
    s_semester=models.CharField(max_length=15)
    s_attendance=models.CharField(max_length=15)
    s_cgpa=models.CharField(max_length=15)
