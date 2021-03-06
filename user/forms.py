from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label= "Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label = 'Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def  clean_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Paswords don\'t match')
            return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

