from django import forms


class UserNameForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        data = self.data
        return data.get('username')
