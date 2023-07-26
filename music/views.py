from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Books
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # 查询:
    # all_book = Books.objects.all()
    all_book = Books.objects.filter(is_active=True)
    # print(all_book.query)


    # 更改:
    # one_book = Books.objects.get(id = 3 )
    # one_book.pub = "邮政出版社"
    # one_book.save()
    # print(one_book.pub)

    # one_book = Books.objects.filter(id = 3)
    # print(one_book[0].pub)
    # one_book.update(pub = "关东出版社")

    return render(request, 'music/index.html', locals())

def article(request):
    return render(request, 'music/article.html')


def play_audio(request):
    return render(request, 'music/demo.html')

# @csrf_protect 没用
@login_required
def create_book(request):
     # 插入:
    book = Books.objects.create(name = "摘眼镜", author = "鲁班", price = 99.225, pub = "东方出版社")
    return render(request, 'music/create_book.html', locals())

# @csrf_exempt
def update_book(request, book_id):
    try:
        book = Books.objects.get(id=book_id, is_active=True)
        # token = get_token(request)
        # print("token:",token)
    except Exception as e:
        print('--update book error is: %s'%(e))
        return HttpResponse('--The book is not exist')

    if request.method == 'GET':

        return render(request, 'music/update_book.html', locals())
    elif request.method == "POST":

        name = request.POST['name']
        price = request.POST['price']

        book.name = name
        book.price = price
        book.save()
        return HttpResponseRedirect('/music/index')


# @csrf_protect 没用
@login_required
def del_book(request, book_id):

    if not book_id:
        return HttpResponse('--请求异常')

    try:
        book = Books.objects.get(Q(id=book_id)&Q(is_active=True))
    except Exception as e:
        print('--delete book get error %s'%(e))
        return HttpResponse('-- The book id is wrong')

    # book.delete()

    book.is_active = False
    book.save()

    return HttpResponseRedirect('/music/index')
