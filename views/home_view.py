import time
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def home(request):
    from django.shortcuts import render
    user = request.user
    if not user.is_anonymous:
        username = user


    return render(request, 'home.html', locals())
