from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")


def pathview(request, name, id):
    return HttpResponse(f"Hello {name}, your id is {id}")


def showform(request):
    return render(request, "form.html")


def getform(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse(f'Name: {name}, Id: {id}')


def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drink.get(drink_name)
    return HttpResponse(f'<h2>{drink_name}</h2><span>{choice_of_drink}</span>')
