from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login_registration/index.html')

def login(request):
    result = User.objects.validateLogin(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('login_registration:index'))

    return log_user_in(request, result[1])

def register(request):
    result = User.objects.validateReg(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('login_registration:index'))

    return log_user_in(request, result[1])

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['logged_in'] = True
    request.session['user'] = user.id
    return redirect('/task')

def logout(request):
    request.session.pop('user')
    return redirect(reverse('index'))
