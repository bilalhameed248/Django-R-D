from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),  #get and Post req for insert operation
    path('list/', views.employee_list, name='employee_list'), #get and Post req for update operation
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
    ]