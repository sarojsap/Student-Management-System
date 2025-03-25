from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('allstudents/', views.all_students, name='all_students'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_selected_students/', views.delete_selected_students, name='delete_selected_students'),
]