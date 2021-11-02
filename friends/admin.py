from django.contrib import admin
from .models import Friends, FriendRequest


# Register your models here.
class FriendsAdmin(admin.ModelAdmin):
    list_display = ["user", "friend", "status"]


class FriendsRequestAdmin(admin.ModelAdmin):
    list_display = ["requester", "receiver"]


admin.site.register(Friends, FriendsAdmin)
admin.site.register(FriendRequest, FriendsRequestAdmin)
