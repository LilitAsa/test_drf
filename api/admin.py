from django.contrib import admin
from .models import Post, Category

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    