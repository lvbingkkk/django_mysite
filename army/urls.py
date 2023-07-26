from . import views
from django.urls import path

urlpatterns = [
    path('', views.hero_list, name='hero_list'),
    path('add_hero/', views.add_hero, name='add_hero'),

]
