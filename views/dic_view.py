import time
def dic(request):
    from django.shortcuts import render
    # dic = {}
    # dic['username'] = "admin"
    # dic['password'] = '123456'
    # return render(request, 'dic.html', dic)

    username = "admin"
    password = '123456'
    year = time.gmtime().tm_year
    return render(request, 'dic.html', locals())
