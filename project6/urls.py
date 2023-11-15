"""
URL configuration for project6 project.

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
from django.urls import path
from app1.views import *
from app2.views import *
from app3.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prasanna1/',prasanna1,name='prasanna1'),
    path('prasanna2/',prasanna2,name='prasanna2'),
    path('prasanna3/',prasanna3,name='prasanna3'),
    path('prasu1/',prasu1,name='prasu1'),
    path('prasu2/',prasu2,name='prasu2'),
    path('prasu3/',prasu3,name='prasu3'),
    

]
