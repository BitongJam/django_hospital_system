"""
URL configuration for hostpital_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),    
    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
]
