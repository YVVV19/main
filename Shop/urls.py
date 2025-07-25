from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login, name='login'),
    path('admin_page/', views.add_product, name='add_product'),
    path('paginator/', views.paginator, name='paginator'),
    path('change-password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
