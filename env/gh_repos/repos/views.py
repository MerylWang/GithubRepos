from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics 

from . models import *
from . serializers import *

# TODO: logic that gets user_id from username and repos from user_id
# user_id = GhUser.objects.get(username="MerylWang").id
# error if username not found 
# Repo.objects.filter(owner_id=46695945)

class RepoView(viewsets.ModelViewSet):
    serializer_class = RepoSerializer
    queryset = Repo.objects.all()


class GhUserView(viewsets.ModelViewSet):
    serializer_class = GhUserSerializer
    queryset = GhUser.objects.all()

# class UserRepoView(viewsets.GenericViewSet):
#     # serializer_class = RepoSerializer
#     # TODO: take username as a parameter
#     # TODO: where should this logic live?
#     user_id = GhUser.objects.get(username="MerylWang").id
#     queryset = Repo.objects.filter(owner_id=user_id)


