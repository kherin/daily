from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Menu


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


def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}
    return render(request, "menu.html", items_dict)


def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', {'content': about_content})
