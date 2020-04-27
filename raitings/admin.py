from django.contrib import admin
from .models import Raiting

class RaitingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('created', 'is_active', 'author')
    search_fields = ('title', 'short_description', 'content', 'author')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'slug',
                'short_description',
                'content',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('author', 'image', 'is_active', 'created', 'views')
            }
            )
    )
admin.site.register(Raiting, RaitingAdmin)