from django.contrib import admin
from .models import *



class ClientsAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "store_name", "email", "phone1", "pic", "gender", "created_on", "updated_on"]
    class Meta:
        model = Clients

class UserWalletAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "wallet_balance", "created_on", "updated_on"]
    class Meta:
        model = UserWallet





admin.site.register(Clients, ClientsAdmin)
admin.site.register(UserWallet, UserWalletAdmin)


