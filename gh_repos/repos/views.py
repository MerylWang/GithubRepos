from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics 

from . models import *
from . serializers import *

# debugger
# import pdb; pdb.set_trace()


# TODO: logic that gets user_id from username and repos from user_id
# user_id = GhUser.objects.get(username="MerylWang").id
# error if username not found 
# Repo.objects.filter(owner_id=46695945)

class RepoView(viewsets.ModelViewSet):
    serializer_class = RepoSerializer
    queryset = Repo.objects.all()

    # def get_user_repos(self, request):
    #     username = request.username
    #     if len(username) < 1:
    #         raise HttpResponseBadRequest('empty username not valid')
    #     try: 
    #         user = GhUser.objects.get(username=username)
    #         return Repo.objects.filter(owner=user.id)
    #     except:
    #         raise HttpResponseNotFound('username {} not found'.format(username))


class GhUserView(viewsets.ModelViewSet):
    serializer_class = GhUserSerializer
    queryset = GhUser.objects.all()

    # def repos(self, request):
    #     username = request.username
    #     if len(username) < 1:
    #         raise HttpResponseBadRequest('empty username not valid')
    #     try: 
    #         user = GhUser.objects.get(username=username)
    #         return Repo.objects.filter(owner=user.id)
    #     except:
    #         raise HttpResponseNotFound('username {} not found'.format(username))


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




