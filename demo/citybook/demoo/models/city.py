from django.db import models


class City(models.Model):

    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
