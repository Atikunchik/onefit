from django.contrib import admin
from rest_framework.authtoken.models import Token


class TokenAdmin(admin.ModelAdmin):
    model = Token