from django.contrib import admin
from .models import *


class EventsListAdmin(admin.ModelAdmin):
    list_display = ["id", "event_organiser", "event", "venue", "timing", "tag", "description", "banner", "price", "gs_points", "created_on", "updated_on"]
    class Meta:
        model = EventsList


class GuestsAdmin(admin.ModelAdmin):
    list_display = ["id", "event", "guest_name", "designation", "pic", "created_on", "updated_on"]
    class Meta:
        model = Guests

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "event", "image", "created_on", "updated_on"]
    class Meta:
        model = ImageGallery


class SubEventsAdmin(admin.ModelAdmin):
    list_display = ["id", "event", "sub_event", "created_on", "updated_on"]
    class Meta:
        model = SubEvents



admin.site.register(EventsList, EventsListAdmin)
admin.site.register(Guests, GuestsAdmin)
admin.site.register(ImageGallery,ImageGalleryAdmin)
admin.site.register(SubEvents, SubEventsAdmin)


