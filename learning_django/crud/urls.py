from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.insert_data, name='insert_data'),  #get and Post req for insert operation
    path('list/', views.list_data, name='list_data'), #get and Post req for update operation
    path('<int:id>/', views.update_data, name='update_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
    ]   