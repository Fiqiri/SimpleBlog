from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'date')
    list_display_links = ('slug',)
    list_filter = ('tags',)
    search_fields = ('slug', 'content')
    list_per_page = 25


admin.site.register(Article, ArticleAdmin)
