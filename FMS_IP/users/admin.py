from django.contrib import admin
from .models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'birth_date', 'slug')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'slug')
    list_filter = ('id', 'username', 'first_name', 'last_name', 'birth_date', 'slug')
    prepopulated_fields = {'slug': ('username', )}

admin.site.register(User, UsersAdmin)