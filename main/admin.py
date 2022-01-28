from django.contrib import admin
from .models import Message


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'message_text', 'created_at')
    list_display_links = ('id', 'author_name')


admin.site.register(Message, MainAdmin)