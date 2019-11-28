from django.contrib import admin
from django.urls import path, re_path
from .views import index

urlpatterns = [
    # RegEx pattern to allow optional use of the trailing slash
    # with APPEND_SLASH as False
    re_path(r'^/?$', index, name='locate_numbers_index'),
]
