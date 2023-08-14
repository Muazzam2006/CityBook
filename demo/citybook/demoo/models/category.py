from django.db import models


class Category(models.Model):

    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", max_length=512)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        # ordering = ['name']
