from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_about(request):
    return render(request, "emp/emphome.html",{})


def emp_add(request):
    return render(request, "emp/addemp.html",{})