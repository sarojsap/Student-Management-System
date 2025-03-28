from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    student_id = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    gpa = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(4.0)])

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')

    course_choices = [
        ('BE CE', 'BE Computer'),
        ('BE Civil', 'BE Civil'),
        ('BE Electronics and Communication', 'BE Electronics and Communication'),
        ('BE IT','BE Information Technology'),
        ('B. Architecture','B. Architecture'),
        ('BCA', 'Bachelor of Computer Application'),
        ('BBA', 'Bachelor of Business Adminstration'),
    ]
    course = models.CharField(max_length=50, choices=course_choices, default='BE CE')

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
