from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'place', )
    list_editable = ('day', 'place', )
    list_filter = ('place', 'created', 'is_active')
    search_fields = ('title', 'short_description', 'content', 'day', 'place')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'slug',
                'short_description',
                'day',
                'place',
                'content',
                'author'
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('start_time', 'end_time', 'image', 'is_active', 'created', 'views')
            }
            )
    )

admin.site.register(Event, EventAdmin)