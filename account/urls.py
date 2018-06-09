from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),


]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)