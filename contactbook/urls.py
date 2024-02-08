"""
URL configuration for contactbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from contact.views import *

urlpatterns = [
    path('',homepage),
    path('contact/',contactpage),
    path('view-data/',view_data),
    path('delete-data/<int:del_id>',delete_data),
    path('edit-data/<int:edit_id>',edit_data),
    path('insert-data/<int:insert_id>',insert),
    path('login/',login),
    path('welcome/',welcome),
    path('view-data/logout/',logout),
    path('admin/', admin.site.urls),
]
