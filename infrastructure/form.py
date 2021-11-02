from django import forms
from .models import PublicKey
from django.contrib.auth.models import User


class AddPublicKeyForm(forms.ModelForm):
    class Meta:
        model = PublicKey
        fields = ('public_key',)
