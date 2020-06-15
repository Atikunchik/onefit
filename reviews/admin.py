from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['id', 'title', 'description', 'rating']

admin.site.register(Review, ReviewAdmin)
#admin.site.register(Token, TokenAdmin)

