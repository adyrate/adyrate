from django.db import models
from accounts.models import *


class StoreProfile(models.Model):
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    info = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    logo = models.ImageField()
    banner = models.ImageField(default='home/dk/Desktop/gluespark/static/img/bg1.jpg')
    ady_points = models.IntegerField()
    ady_points_given = models.IntegerField()
    ady_points_redeemed = models.IntegerField()

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.store.store_name

class Discounts(models.Model):
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    discount_percentage = models.IntegerField()
    ady_points = models.IntegerField()
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.store.store_name


class Gallery(models.Model):
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.store.store_name


class Menu(models.Model):
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.store.store_name


