from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'created_at')
    list_display_links = ('title', 'created_at')
    search_fields = ('id', 'title', 'description', 'slug', 'preparation_steps')
    list_filter = ('is_published', 'author', 'category', 'preparation_steps_is_html')
    list_per_page = 5
    list_editable = ('is_published',)
    ordering = ('-id',)
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
