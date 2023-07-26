from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('play_audio/',views.play_audio,name='play_audio'),
    path('article/',views.article),

    path('create_book/',views.create_book),
    path("update_book/<int:book_id>/", views.update_book),
    path('del_book/<int:book_id>/', views.del_book)
]
