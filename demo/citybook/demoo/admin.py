from django.contrib import admin
from .models import Handbook
from .models import Contact
from .models import City
from .models import Category

# Register your models here.


@admin.register(Handbook)
class HandbookAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "description", "address", "city"]
    list_filter = ["name", "category", "address", "city"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["cName",  "phone1", "phone2", "email"]
    list_filter = ["cName"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
