from rest_framework import serializers
from . models import *

"""
convert model instances to JSON so that the frontend can work with the received data
"""
class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo 
        fields = ('id', 'name', 'description', 'language', 'stargazers_count', 'forks_count', 'html_url', 'owner_id') 

class GhUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhUser 
        fields = ('id', 'username', 'html_url') 

