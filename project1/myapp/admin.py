from django.contrib import admin

from myapp.models import Person, Drinks, DrinksCategory

# Register your models here.
admin.site.register(Person)
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
