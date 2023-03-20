from django.contrib import admin
from .models import GhUser, Repo

admin.site.register(Repo)
admin.site.register(GhUser)
