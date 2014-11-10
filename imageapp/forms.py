from django import forms
from django.forms import ModelForm
from imageapp.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200)

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'second_name', 'password')



