from django.contrib import admin
from .models import Category, Location, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'location', 'pub_date', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',
                   'location', 'pub_date', 'created_at')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'text', 'author', 'image')
        }),
        ('Категоризация', {
            'fields': ('category', 'location')
        }),
        ('Публикация', {
            'fields': ('pub_date', 'is_published')
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text_short', 'created_at')
    list_filter = ('created_at', 'post__category')
    search_fields = ('text', 'post__title', 'author__username')
    raw_id_fields = ('post', 'author')

    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text

    text_short.short_description = 'Текст комментария'
