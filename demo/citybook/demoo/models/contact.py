from django.db import models


class Contact(models.Model):

    # cName = models.CharField("Contact name", max_length=50)
    # handbook = models.OneToOneField("handbook", on_delete=models.CASCADE, related_name="contacts")
    phone1 = models.CharField('First phone', max_length=20)
    phone2 = models.CharField('Second phone', max_length=20)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        # ordering = ['', '']

    def __str__(self) -> str:
        return self.email
