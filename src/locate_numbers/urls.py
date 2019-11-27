from django.contrib import admin
from django.urls import path, re_path
from .views import helloWorld

urlpatterns = [
    re_path(r'^/?$', helloWorld),
]
