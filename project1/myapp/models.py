from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        DrinksCategory, on_delete=models.PROTECT, default=None)


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='Vehicle')
