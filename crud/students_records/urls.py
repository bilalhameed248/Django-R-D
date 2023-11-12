from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('insert_student/', views.insert_student, name='insert_student'),
    path('edit_student/', views.edit_student, name='edit_student'),
    # path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('insert_section/', views.insert_section, name='insert_section'),
]