from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def base(request):
    return render(request, 'animation/base.html')

def one(request):
    return render(request, 'animation/one.html')

def two(request):
    return render(request, 'animation/two.html')

def three(request):
    return render(request, 'animation/three.html')

@csrf_exempt
def turnNum(request):
    if request.method == "GET":
        return render(request, 'animation/turnNum.html')

    if request.method == "POST":
        try:

            num =int(request.POST['inputValue'],0)
            # num =request.POST['inputValue'].strip()
            # # print(num[0:2])
            # if num[:2] == '0b' or num[:2] == '0B':
            #     num = int(num, 2)
            # elif num[:2] == '0o' or num[:2] == '0O':
            #     num = int(num, 8)
            # elif num[:2] == '0x' or num[:2] == '0X':
            #     num = int(num, 16)
            # else:
            #     num = int(num)
            res = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(num,num,num,num)
            # res = "int: %d,  hex: %x,  oct: %o,  bin: %s"%(num,num,num,bin(num))
            print(res)
            return render(request, 'animation/turnNum.html', locals())
        except Exception as e:
            print(e)
            return HttpResponse('请输入真确的数字格式')
