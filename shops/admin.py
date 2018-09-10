from django.contrib import admin
from .models import *


class StoreProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "store", "info", "address", "logo", "banner", "ady_points", "ady_points_given", "ady_points_redeemed", "created_on", "updated_on"]
    class Meta:
        model = StoreProfile


class DiscountsAdmin(admin.ModelAdmin):
    list_display = ["id", "store", "discount_percentage", "ady_points", "status", "created_on", "updated_on"]
    class Meta:
        model = Discounts

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "store", "image", "created_on", "updated_on"]
    class Meta:
        model = Gallery

class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "store", "image", "created_on", "updated_on"]
    class Meta:
        model = Menu


admin.site.register(StoreProfile, StoreProfileAdmin)
admin.site.register(Discounts, DiscountsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Menu, MenuAdmin)




