"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, admindocs
from django.contrib.admindocs import urls as admin_doc
from django.urls import path, re_path, include
from django.views import debug
# print('admin urls:',admin.site.urls)
# print('admin site:',admin.site)
# print('admin :',admin)

from views import dic_view, home_view
from django.contrib.auth import views


urlpatterns = [
    path('', dic_view.dic),
    path('home/', home_view.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('admin_doc/', include(admin_doc)),
    # path('page/<int:pg>/', debug.page),
    path('dic/abc/', dic_view.dic, name='dict'),
    # re_path(r'^page/(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})',debug.page)

    path('music/', include('music.urls')),
    path('user/', include('user.urls')),
    path('note/', include('note.urls')),
    path('animation/', include('animation.urls')),
    path('army/', include('army.urls')),

    # 来自contrib/auth/urls.py
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),



]
