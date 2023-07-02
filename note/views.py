from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Note


# from note.check import check_login

# # Create your views here.

# @check_login
@login_required
def list_view(request):
    author = request.user
    notes = author.note_set.all()
    print(notes)
    try:
        content = notes[0].content
        print(content)
    except Exception as e:
        print(e)

    return render(request,'note/list.html', locals())

@csrf_exempt
@login_required
def add_note(request):
    # author = request.user.id
    author = request.user

    # print(type(author))
    if request.method== 'GET':
        return render(request,'note/add_note.html', locals())
    if request.method == 'POST':
        author_id = request.POST['author_id']
        title = request.POST['title']
        #encode()以后拿数据还费劲..没encode 也存了!!!!
        # content = request.POST['content'].encode()
        content = request.POST['content']

        # Note.objects.create(title=title, content=content, author_id=author_id)
        #也可以:
        Note.objects.create(title=title, content=content, author=author)

        return HttpResponseRedirect('/note')
