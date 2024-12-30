"""
URL configuration for Topic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpages/',insert_webpages,name='insert_webpages'),
    path('insert_Record/',insert_Record,name='insert_Record'),
    path('Display_topic/',Display_topic,name='Display_topic'),
    path('Display_webpage/',Display_webpage,name='Display_webpage'),
    path('Display_record/',Display_record,name='Display_record'),
]
