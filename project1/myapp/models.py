from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
