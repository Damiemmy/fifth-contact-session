from django.contrib import admin
from .models import Category, MediaItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "category", "creator", "created_at", "views")
    list_filter = ("media_type", "category", "created_at")
    search_fields = ("title", "description", "creator")
    readonly_fields = ("created_at", "views")
