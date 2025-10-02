"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from blog import views as blog_views
from carapp import views as carapp_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='index'),
    path('body/', blog_views.body, name='body'),
    path("button/", blog_views.button, name="button"),
    path('post_list/', blog_views.show_post, name='post_list'),
    path('myposts/', blog_views.show_post, name='myposts'),
    path('car_list/', carapp_views.car_list, name='car_list'),
    path('add_post/', blog_views.add_post, name='add_post'),
    path('myposts/<int:id>/', blog_views.find_post, name='postdetail'),
]
