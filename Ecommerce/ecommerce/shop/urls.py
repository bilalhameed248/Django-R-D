from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="aboutUs"),
    path('contact/', views.contact, name="contactUs"),
    path('tracker/', views.tracker, name="trackingStatus"),
    path('search/', views.search, name="search"),
    path('productview/', views.productview, name="productView"),
    path('checkout/', views.checkout, name="checkOut"),
]