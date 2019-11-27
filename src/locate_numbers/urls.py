from django.contrib import admin
from django.urls import path, re_path
from .views import index

urlpatterns = [
    # Patrón usando regex para permitir el uso o desuso de trailing slash
    re_path(r'^/?$', index),
]
