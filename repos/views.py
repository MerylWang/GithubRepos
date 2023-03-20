from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics 

from . models import *
from . serializers import *

class RepoView(viewsets.ModelViewSet):
    serializer_class = RepoSerializer
    queryset = Repo.objects.all()

class GhUserView(viewsets.ModelViewSet):
    serializer_class = GhUserSerializer
    queryset = GhUser.objects.all()

class UserReposView(generics.ListAPIView):
    serializer_class = RepoSerializer
    def get_queryset (self):
        username = self.kwargs['username']

        if len(username) < 1:
            raise HttpResponseBadRequest('empty username not valid')
        try: 
            user = GhUser.objects.get(username=username)
            return Repo.objects.filter(owner=user.id)
        except:
            raise HttpResponseNotFound('username {} not found'.format(username))




