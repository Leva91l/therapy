from django.contrib import admin
from .models import *

class MainAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'content']
    list_display_links = ['content']
    search_fields = ['name']


admin.site.register(Category, MainAdmin)
