from django import forms
from django.forms import ModelForm
from imageapp.models import User
from imageapp.models import Settings


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'second_name', 'password')
        widgets = {'password': forms.PasswordInput(),}


class SettingsForm(forms.Form):
    image = forms.ImageField(required=True)

class PicturesForm(forms.Form):
    image = forms.ImageField(required=True)
