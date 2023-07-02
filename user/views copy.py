from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import User
from django.views.decorators.csrf import csrf_exempt
import  hashlib
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

        #哈希算法 - 给定明文,计算出一段定长,不可逆的值 ; md5,sha-256
        m = hashlib.md5(pa_1.encode())
        password_m = m.hexdigest()

        #当前用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已存在')

        #唯一索引 并发 写入问题
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('--create user error %s'%(e))
            return HttpResponse('用户已注册')

        # 免登陆一天
        request.session['username'] = username
        #主键查询比唯一索引快:
        request.session['uid'] = user.id

        #todo 修改session的存储时间?:

        # return HttpResponse('注册成功')
        return HttpResponseRedirect('/home')

@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        # print('keys:',request.session.keys())

        #检查登陆状态,如果登陆了显示 ‘已登陆’
        if request.session.get('username') and request.session.get('uid'):
            # print(request.session.keys())
            print('item:',request.session.items())
            # print('value:',request.session.values())
            return HttpResponseRedirect('/home')

        #检查Cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            #回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登陆')
            return HttpResponseRedirect('/home')


        return render(request, 'user/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('用户名或密码错误!')

        #对比密码
        m = hashlib.md5(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误!')

        #记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        # resp = HttpResponse('登陆成功!!')
        resp = HttpResponseRedirect('/home')

        #判断用户是否点选了记住我
        if  'remember' in request.POST:
            resp.set_cookie('username',username, 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)
        #选了 cookie 存储 username uid 三天

        return resp

def logout_view(request):
    if 'username' in request.session or 'uid' in request.session :
        request.session.flush()
    # if 'username' in request.session:
    #     del request.session['username']
    # if 'uid' in request.session :
    #     del request.session['uid']

    resp = HttpResponseRedirect('/home')

    if 'username' in request.COOKIES :
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
