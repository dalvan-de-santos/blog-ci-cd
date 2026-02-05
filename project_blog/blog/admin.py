from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=('name', 'description', 'tags', 'created_at', 'updated_at')
    list_filter=('tags', 'name')
    search_fields=('name', 'tags')

