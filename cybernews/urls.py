
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news import views

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.show_recent_article, name='main-page'),
    path('', include('news.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)