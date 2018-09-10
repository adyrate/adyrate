from django.db import models
from django.contrib.auth.models import User


class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    wallet_balance = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username





class Clients(models.Model):
    full_name = models.CharField(max_length=50)
    store_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    phone1 = models.IntegerField()
    pic = models.ImageField()

    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(choices=gender_options, max_length=6)

    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.store_name





