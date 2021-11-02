from django import forms


class StoreDataForm(forms.Form):
    toUsername = forms.CharField()
    plaintext = forms.CharField()
