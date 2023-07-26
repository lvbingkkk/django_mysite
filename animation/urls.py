from django.urls import path
from . import views
urlpatterns = [
    path('base/',views.base, name='base'),
    path('one/',views.one, name='one'),
    path('two/',views.two, name='two'),
    path('three/',views.three, name='three'),
    path('turnNum/',views.turnNum, name='turnNum'),


]
