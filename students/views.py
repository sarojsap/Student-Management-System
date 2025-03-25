from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    latest_students = Student.objects.all().order_by('-id')[:6] #order by 'id' in descending order and get the latest 5
    return render(request, 'students/index.html', {
        'students': latest_students
    })

def all_students(request):
    all_students = Student.objects.all()
    return render(request, 'students/all_students.html', {
        'students': all_students
    })

def delete_selected_students(request):
    if request.method == 'POST':
        selected_students = request.POST.getlist('selected_students')
        Student.objects.filter(id__in=selected_students).delete()
    return HttpResponseRedirect(reverse('all_students'))

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_id = form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_course = form.cleaned_data['course']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_id = new_student_id,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                course = new_course,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'students/add.html',{
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html',{
        'form': StudentForm()
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html',{
                'form':form,
                'success':True
            })  
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html',{
        'form':form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))