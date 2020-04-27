from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', )
    list_filter = ('user', )


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', )


class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', )
    list_editable = ('link', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ('is_active', )
    list_filter = ('name', 'is_active')
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'is_active',)
    list_editable = ('is_active', )
    list_filter = ('category', 'created', 'is_active')
    search_fields = ('title', 'short_description', 'content', 'author',  'category')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'slug',
                'short_description',
                'category',
                'content',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('author', 'integer_of_day', 'image', 'is_active', 'created', 'views')
            }
            )
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Subscribe, SubscribeAdmin)