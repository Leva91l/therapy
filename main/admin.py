from django.contrib import admin

from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'content']
    list_display_links = ['content']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'photo']
    list_display_links = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, MainAdmin)
admin.site.register(Product, ProductAdmin)
