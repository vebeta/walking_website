from django.contrib import admin
from .models import *


class TrailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'rate', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('id', 'title', 'date', 'rate', 'is_published')
    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Trail, TrailsAdmin)
admin.site.register(Category, CategoryAdmin)