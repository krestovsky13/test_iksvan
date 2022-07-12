from django.contrib import admin

from .models import Urls


@admin.register(Urls)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_url', 'short_url', 'user']
    readonly_fields = ('short_url',)
