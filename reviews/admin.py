from django.contrib import admin
from .models import Review
from rest_framework.authtoken.models import Token


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['title', 'description', 'rating']


class TokenAdmin(admin.ModelAdmin):
    model = Token


admin.site.register(Review, ReviewAdmin)
#admin.site.register(Token, TokenAdmin)

