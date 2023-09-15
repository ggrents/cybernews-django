from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users import views

from cybernews import settings

urlpatterns = [

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('pass-change/', views.PasswordChange.as_view(), name='change-password'),


]