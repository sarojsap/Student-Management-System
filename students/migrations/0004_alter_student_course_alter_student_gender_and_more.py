# Generated by Django 5.1.7 on 2025-03-28 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('BE CE', 'BE Computer'), ('BE Civil', 'BE Civil'), ('BE Electronics and Communication', 'BE Electronics and Communication'), ('BE IT', 'BE Information Technology'), ('B. Architecture', 'B. Architecture'), ('BCA', 'Bachelor of Computer Application'), ('BBA', 'Bachelor of Business Adminstration')], default='BE CE', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(4.0)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
