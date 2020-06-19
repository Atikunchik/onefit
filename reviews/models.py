from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Review(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=10000)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)

    def full(self):
        return {
            'title': self.title,
            'rating': self.rating,
            'description': self.description,
            'company': self.company.name,
            'user': self.user.id,
        }