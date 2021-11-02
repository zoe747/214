from django.contrib import admin
from .models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ["is_received", "fromUser", "toUser", "plaintext"]


admin.site.register(Message, MessageAdmin)
