"""
URL configuration for UrbanDjango project.

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
#from task2.views import index_func, index_class
#from task3.views import platform, games_store, cart_of_store
from task4.views import platform, games_store, cart_of_store

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', index_func),
    #path('index/', index_class.as_view())
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', platform),
    path('games/', games_store),
    path('cart/', cart_of_store),
]

#  python manage.py runserver