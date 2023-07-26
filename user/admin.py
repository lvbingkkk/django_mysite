from django.contrib import admin

from django.contrib.auth.models import User, UserManager
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from django.core import mail

from django.conf import settings
# Register your models here.

def create_user(request):
    # user = User.objects.create_user(username='usertest', password='123456')
    # print('user',user)
    return HttpResponse('/home')

def sendMail(request):

    res = send_mail(
        "Subject here",
        "Here is the message.two",
        # "443647090@qq.com",
        settings.EMAIL_HOST_USER,

        ["klvong@icloud.com",'1871981239@qq.com'],
        # fail_silently=False,
        # auth_user='443647090@qq.com',
        # auth_password='bing??6117',
        # connection=None
    )

    # with mail.get_connection() as connection:
    #     mail.EmailMessage(
    #         "Subject here",
    #         "Here is the message.000",
    #         "443647090@qq.com",
    #         ["klvong@icloud.com"],
    #         connection=connection,
    # ).send()
    return render(request, 'user/sendMail.html', locals())
