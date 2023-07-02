from . import views, admin
from django.urls import path

urlpatterns = [
    path('reg/', views.reg_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('create_user', admin.create_user)
]
