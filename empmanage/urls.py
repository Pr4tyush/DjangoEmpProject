from django.contrib import admin
from django.urls import path,include
from .views import*

urlpatterns = [
    path("about/",emp_about),
    path("addemp/",emp_add),
]