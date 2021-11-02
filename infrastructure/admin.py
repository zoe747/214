from django.contrib import admin
from .models import PublicKey


# Register your models here.
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = ["user", "public_key"]


admin.site.register(PublicKey, PublicKeyAdmin)
