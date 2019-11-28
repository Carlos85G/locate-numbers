"""check_numbers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from locate_numbers import urls as ln_urls
from .views import index

urlpatterns = [
    # Admins are not used
    # path('admin/', admin.site.urls),
    # RegEx pattern to allow optional use of the trailing slash
    # with APPEND_SLASH as False
    re_path(r'^/?$', index, name='locate_numbers_index'),
    # Append app's URLs to main project
    path('locate_numbers', include("locate_numbers.urls")),
]
