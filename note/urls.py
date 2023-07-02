from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_view, name='note'),
    path('add_note/', views.add_note, name='add_note'),


]
