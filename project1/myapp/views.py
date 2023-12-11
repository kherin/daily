from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")


def pathview(request, name, id):
    return HttpResponse(f"Hello {name}, your id is {id}")


def showform(request):
    return render(request, "form.html")
