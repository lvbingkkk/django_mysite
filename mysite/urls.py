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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views import debug
# print('admin urls:',admin.site.urls)
from views import dic_view, home_view

urlpatterns = [
    path('', dic_view.dic),
    path('home/', home_view.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('page/<int:pg>/', debug.page),
    path('dic/abc/', dic_view.dic, name='dict'),
    # re_path(r'^page/(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})',debug.page)

    path('music/', include('music.urls')),
    path('user/', include('user.urls')),
    path('note/', include('note.urls'))

]
