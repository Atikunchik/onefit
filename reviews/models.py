from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


class Review(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
