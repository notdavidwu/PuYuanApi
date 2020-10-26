"""PuYuanApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Denru.views import *
from info.views import *
from blood.views import *

urlpatterns = [
    #Denru
    path('admin/', admin.site.urls),
    path('api/register/check/', RegCheck),
    path('api/user/privacy-policy/', pp),
    path('api/register/', Reg),
    path('api/auth/', login),
    path('api/verification/send/', sendcode),
    path('api/verification/check/', codechecking),
    path('api/password/forgot/', forget),
    path('api/password/reset/', reset),
    #info
    path('api/user/', information),
    path('api/user/default/', individualdefault),
    path('api/user/a1c/', a1c),
    path('api/user/drug-used/', medicine),
    path('api/user/medical/', mediinfo),
    path('api/news/', news),
    path('api/user/badge/', bage),
]
