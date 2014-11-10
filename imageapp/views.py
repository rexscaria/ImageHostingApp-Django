from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from imageapp.models import User
from imageapp.models import Picture

SESSION_KEY = settings.SESSION_KEY

def index(request):
    if SESSION_KEY in request.session:
        return redirect('home')
    return redirect('login')


def login(request):
    remove_session(request)
    return render(request, 'login.html')


# private

def remove_session(request):
    if SESSION_KEY in request.session:
        del request.session[SESSION_KEY]

# Create your views here.
