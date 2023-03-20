from django.db import models
# TODO: add uniqueness constraint to username
# TODO: add created_at and updated_at to Repo 

class GhUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    html_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username 

class Repo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    stargazers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    html_url = models.URLField(blank=True, null=True)
    owner = models.ForeignKey('GhUser', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name 







