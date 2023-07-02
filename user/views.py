from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@csrf_exempt
def reg_view(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        pa_1 = request.POST['password_1']
        pa_2 = request.POST['password_2']

        if pa_1 != pa_2:
            return HttpResponse('两次密码不一致')

        #当前用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已存在')

        #唯一索引 并发 写入问题
        try:
            user = User.objects.create_user(username=username, password=pa_1)
        except Exception as e:
            print('--create user error %s'%(e))
            return HttpResponse('用户已注册')

        # 免登陆一天
        login(request, user)
        #todo 修改session的存储时间?:

        # return HttpResponse('注册成功')
        return HttpResponseRedirect('/home')

@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        print('keys:',request.session.keys())
        print('item:',request.session.items())
        print('usr:',request.user.get_username)
        print('usr:',request.user)

        #检查登陆状态,如果登陆了显示 ‘已登陆’
        if not request.user.is_anonymous:
            return HttpResponseRedirect('/home')

        return render(request, 'user/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if not user:
            return HttpResponse('用户名或密码错误!')
        else:
            login(request, user)
            return HttpResponseRedirect('/home')

@login_required
def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/home')
