
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news import views

from cybernews import settings

urlpatterns = [
    path('', views.show_article.as_view(), name='main-page'),
    path('detail/<int:id>', views.article_detail, name='full-article'),
    path('onlycat/<slug:slug>/', views.show_only_category, name='category-only'),
    path('addart/', views.addart, name='addart'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('tagsearch/<str:tag>/', views.show_article_byTags, name = 'tag_search')


]