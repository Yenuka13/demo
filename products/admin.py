from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description')


admin.site.register(Product, ProductAdmin)
