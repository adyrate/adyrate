from django.db import models
from accounts.models import *

class EventsList(models.Model):
    event_organiser = models.ForeignKey(Clients, on_delete=models.PROTECT)
    event = models.CharField(max_length=30)
    venue = models.CharField(max_length=50)
    timing = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    banner = models.ImageField()
    price = models.IntegerField()
    gs_points = models.IntegerField()

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.event

class Guests(models.Model):
    event = models.ForeignKey(Clients, on_delete=models.PROTECT)
    guest_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50)
    pic = models.ImageField()

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.event

class ImageGallery(models.Model):
    event = models.ForeignKey(Clients, on_delete=models.PROTECT)
    image = models.ImageField()

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.event


class SubEvents(models.Model):
    event = models.ForeignKey(Clients, on_delete=models.PROTECT)
    sub_event = models.CharField(max_length=30)

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.event




