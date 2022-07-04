from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['pk', 'content', 'author']