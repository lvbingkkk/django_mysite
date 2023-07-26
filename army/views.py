from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Role, Hero
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def hero_list(request):
    user = request.user
    heros = Hero.objects.filter(user_id=user.id)
    roles = Role.objects.all()

    print("heros:",heros)
    return render(request, 'army/hero_list.html', locals())

@csrf_exempt
@login_required
def add_hero(request):
    if request.method == "GET":
        roles = Role.objects.all()
        return render(request, 'army/add_hero.html', locals())
    if request.method == "POST":
        name = request.POST['name']
        if Hero.objects.filter(name=name):
            return HttpResponse('该名字已被占用')

        role_id = request.POST['role_id']
        user = request.user

        Hp = Role.objects.get(id=role_id).Hp
        Mp = Role.objects.get(id=role_id).Mp
        Level = Role.objects.get(id=role_id).Level
        Damage = Role.objects.get(id=role_id).Damage
        Defence = Role.objects.get(id=role_id).Defence
        Hero.objects.create(name=name, user=user, role_id=role_id, Mp=Mp, Hp=Hp, Level=Level, Damage=Damage, Defence=Defence )

        return  HttpResponseRedirect('/army')

