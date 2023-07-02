from django.contrib import admin

from django.contrib.auth.models import User, UserManager
from django.http import HttpResponse
# Register your models here.

def create_user(request):
    # user = User.objects.create_user(username='usertest', password='123456')
    # print('user',user)
    return HttpResponse('/home')
