"""
URL configuration for happiness_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from happiness_app import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.index, name="index"),
    path('accounts/', include('allauth.urls')),
    path('acts_of_kindness/', include('acts_of_kindness.urls')),
    path('profile/', include('profiles.urls')),
]
