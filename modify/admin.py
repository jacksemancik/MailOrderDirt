from django.contrib import admin
from storefrontend.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Products, ProductsAdmin)
