from django.contrib import admin
from .models import *



class ReviewsAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "user", "rating", "food_quality", "value_for_money", "hygiene", "service", "comment", "created_on", "updated_on"]
    class Meta:
        model = Reviews



class TempReviewsAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "cookie", "rating", "food_quality", "value_for_money", "hygiene", "service", "comment", "created_on", "updated_on"]
    class Meta:
        model = TempReviews


class CreditTransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "client", "credited_ady_points", "created_on", "updated_on"]
    class Meta:
        model = CreditTransaction


class CouponsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "store", "ady_points_cost", "discount_percentage", "status", "created_on", "updated_on"]
    class Meta:
        model = Coupons

class RedeemTransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "store", "discount_percentage", "before_discount", "discount", "after_discount", "created_on", "updated_on"]




class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "designation", "pic", "rating", "created_on", "updated_on"]
    class Meta:
        model = Testimonials




admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(TempReviews, TempReviewsAdmin)
admin.site.register(CreditTransaction, CreditTransactionAdmin)
admin.site.register(Coupons, CouponsAdmin)
admin.site.register(RedeemTransaction, RedeemTransactionAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)

