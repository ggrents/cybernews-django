from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from forum.views import *
urlpatterns = [

    path("", main_forum, name='main-forum')
]