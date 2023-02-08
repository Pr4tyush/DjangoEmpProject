from django.http import HttpResponse
from django.shortcuts import render
def test(request):
    
    print("this is the first text from view")
    # return HttpResponse("<h1>Hey There!</h1>")
    return render(request, "home.html",{})



def about(request):

    if request.method == 'POST':
        check = request.POST['check']
        print(check)
        
    isActive = True
    name = "Pratyush kumar"
    list_of_programs = [
        "WAP to delete the puncutations"
        "WAP to write a proagram of HelloWorld"
        "WAP to Enter your Name"
    ]
    student={
        'student_name': "Pratyush",
        'student_college': "NIET",
        'student_add': "bihar"

    }
    data= {
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student':student



    }
    # return HttpResponse("<h2>Hello  My name is Pratyush</h2>")
    return render(request, "about.html",data)


def services(request):
    # return HttpResponse("<h2>We provide russians as services</h2>")
    return render(request, "services.html",{})