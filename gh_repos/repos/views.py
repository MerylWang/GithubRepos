from django.shortcuts import render

from . import views

from django.contrib import admin
from django.urls import include, path

# urlpatterns = [
#     path('polls/', include('polls.urls')),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', views.index, name='index'),
]
# Create your views here.
