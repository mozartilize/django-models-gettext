from django.db import models
from django_models_gettext.django import Translatable, TranslationOptions


class Product(Translatable, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(mull=True)

    class Meta:
        translation = TranslationOptions(
            fields=("name", "description"),
        )