from django.db import models
from accounts.models import *
from django.contrib.auth.models import User
from shops.models import *



class Reviews(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.FloatField()
    food_quality= models.FloatField()
    value_for_money = models.FloatField()
    hygiene = models.FloatField()
    service = models.FloatField()
    comment = models.CharField(max_length=300, default="no data for now")

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.client.store_name


class TempReviews(models.Model):
    client= models.ForeignKey(Clients, on_delete=models.PROTECT)
    cookie = models.IntegerField()
    rating = models.FloatField()
    food_quality= models.FloatField()
    value_for_money = models.FloatField()
    hygiene = models.FloatField()
    service = models.FloatField()
    comment = models.CharField(max_length=300, default="no data for now")

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.client.store_name


class CreditTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Clients, on_delete=models.PROTECT)
    credited_ady_points = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username



class Coupons(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    ady_points_cost = models.IntegerField()
    discount_percentage = models.IntegerField()
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)



class RedeemTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    store = models.ForeignKey(Clients, on_delete=models.PROTECT)
    discount_percentage = models.IntegerField()
    before_discount = models.IntegerField()
    discount = models.IntegerField()
    after_discount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username



class Testimonials(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pic = models.ImageField()
    testimonial = models.CharField(max_length=500)
    designation = models.CharField(max_length=30)
    rating = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.full_name