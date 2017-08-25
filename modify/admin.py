from django.contrib import admin
from storefrontend.models import Products, Skills, About, ContactModel

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title','description','icon',)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('about',)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','subject',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
