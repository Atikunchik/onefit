from django.contrib import admin
from .models import Review, Company


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['id', 'title', 'description', 'rating']


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'description']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(Token, TokenAdmin)

