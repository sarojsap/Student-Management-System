from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name','last_name', 'email', 'course', 'gpa']
        labels = {
            'student_id':'Student ID',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'course':'Course',
            'gpa':'GPA',
        }

        """A widget is Django's representation of an HTML input element.
        The widget handles the rendering of the HTML, and extraction of 
        data from a GET/POST dictionary that corresponds to the widget"""
        widgets = {
            'student_id': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'course': forms.TextInput(attrs={'class':'form-control'}),
            'gpa':forms.NumberInput(attrs={'class':'form-control'}),
        }