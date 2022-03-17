from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Comment)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'allowed_comment', 'number_of_likes', 'number_of_save')
    list_filter = ('created', 'category', 'allowed_comment')
    search_fields = ('titles', 'category')
    prepopulated_fields = {'slug': ('title',)}
