from django.db import models
# from django.db.models.query import QuerySet

# class HandbookManager(models.Manager):

#     def by_name(self, categ_name) -> QuerySet:
#         return self.get_queryset().filter(category__name = categ_name)


class Handbook(models.Model):

    name = models.CharField("Name", max_length=100)
    description = models.TextField('Description')
    address = models.CharField('Address', max_length=50)
    city = models.ForeignKey("city", on_delete=models.CASCADE, verbose_name="city")
    contact = models.OneToOneField("contact", on_delete=models.CASCADE, verbose_name="contact")
    category = models.ForeignKey("category", on_delete=models.CASCADE, verbose_name="category")

    # handbook = HandbookManager()
    # objects = models.Manager()

    class Meta:
        verbose_name = "Handbook"
        verbose_name_plural = "Handbooks"
        ordering = ['name', 'city']

    def __str__(self) -> str:
        return self.name
