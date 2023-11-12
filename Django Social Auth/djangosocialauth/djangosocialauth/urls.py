"""djangosocialauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from googleauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.app_home, name='home'),
    path('simple_signup/', views.simple_signup, name='simple_signup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.google_login),

    path("emailvarification/", views.emailvarification, name="emailvarification"),
    # # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('social-auth/', include(('googleauth.urls','googleauth'), namespace="googleauth")),
    path("dictionary", views.dictionary, name="dictionary"),
]
