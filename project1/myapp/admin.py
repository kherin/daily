from django.contrib import admin

from myapp.models import Person, Drinks, DrinksCategory, Customer, Vehicle

# Register your models here.
admin.site.register(Person)
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Customer)
admin.site.register(Vehicle)
