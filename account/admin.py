from django.contrib import admin
from .models import Profile, Devices


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "bio"]


class DevicesAdmin(admin.ModelAdmin):
    list_display = ["user", "last_login_time", "device_uid", "token"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Devices, DevicesAdmin)
