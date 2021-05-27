from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from TrueQuest import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:room_id>/', views.room, name='room'),
    path('room/<int:room_id>/book', views.book_room, name='book_room'),
    path('language/<str:language>', views.change_language, name='change_language'),
    path('admin/', admin.site.urls),
    path('franchise/', views.franchise, name='franchise'),
    path('about/', views.about, name='about')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

