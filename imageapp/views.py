from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from imageapp.forms import LoginForm
from imageapp.forms import RegisterForm
from imageapp.forms import SettingsForm
from imageapp.forms import PicturesForm
from django.contrib import messages
from django.forms.formsets import formset_factory


from imageapp.models import User
from imageapp.models import Settings
from imageapp.models import Picture

from django.forms.util import ErrorList

SESSION_KEY = settings.SESSION_KEY

def index(request):
    if SESSION_KEY in request.session:
        return redirect('home')
    return redirect('login')


def login(request):
    remove_session(request)
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if login_form.is_valid():
            user = User.return_valid_user(email_address=request.POST['email'], raw_password=request.POST['password'])
            if user != None:
                request.session[SESSION_KEY] = user.id
                return redirect('home')

            errors = login_form._errors.setdefault("email", ErrorList())
            errors.append("Login Error!")
        return render(request, 'login.html', {'login_form': login_form, 'registration_form' : RegisterForm()})
    else:
        registration_form = RegisterForm()

    return render(request, 'login.html', {'login_form': login_form, 'registration_form' : registration_form, 'user' : None})

def register(request):
    reg_form = RegisterForm(request.POST or None)
    if request.method == 'POST' and reg_form.is_valid():
        user = reg_form.save(commit=False)
        user.save()
        reg_form = RegisterForm()
        messages.add_message(request, messages.SUCCESS, 'Registration success. Proceed to login')
    return render(request, 'login.html', {'login_form': LoginForm(), 'registration_form' : reg_form})


def home(request):
    if check_login(request) == False:
        return redirect('login')
    current_user = User.objects.get(id=request.session[SESSION_KEY])
    pictures = current_user.pictures
    return render(request, 'home.html', {'pictures': pictures.all(), 'user': current_user})


def logout(request):
    remove_session(request)
    messages.add_message(request, messages.SUCCESS, 'See you later. Login anytime you wish')
    return redirect('login')

def settings(request):
    if check_login(request) == False:
        return redirect('login')
    current_user = User.objects.get(id=request.session[SESSION_KEY])
    settings_form = SettingsForm()

    if request.method == 'POST':
        settings_form = SettingsForm(request.POST, request.FILES)
        if settings_form.is_valid():
            settings = Settings.objects.get_or_create(user=current_user)[0]
            settings.profile_pic = settings_form.cleaned_data['image']
            settings.save()
            messages.add_message(request, messages.SUCCESS, 'Profile image updated')

    user_settings = current_user.settings.all()
    user_settings = user_settings[:1].get() if user_settings.exists() else None

    return render(request, 'settings.html', { 'user': current_user, 'form': settings_form, 'settings' : user_settings})


def upload(request):
    if check_login(request) == False:
        return redirect('login')

    current_user = User.objects.get(id=request.session[SESSION_KEY])
    upload_form = PicturesForm()
    #upload_form = Upload_Form(request.POST, request.FILES or None)
    if request.method == "POST":
        upload_form = PicturesForm(request.POST, request.FILES)
        if upload_form.is_valid() :
            picture = Picture(user=current_user)
            picture.photo = upload_form.cleaned_data['image']
            picture.save()
            messages.add_message(request, messages.SUCCESS, 'Uploaded successfully. Visit home page to see the change.')

    return render(request, 'upload.html', { 'user': current_user, 'form': upload_form})



def contact(request):
    current_user = None
    if check_login(request):
        current_user = User.objects.get(id=request.session[SESSION_KEY])
    return render(request, 'contact.html', { 'user': current_user})



# private

def check_login(request):
    return SESSION_KEY in request.session

def remove_session(request):
    if SESSION_KEY in request.session:
        del request.session[SESSION_KEY]

# Create your views here.
