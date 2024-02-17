from django.contrib import admin
from news.models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author', 'views', 'created_date', 'status', 'published_date')
    list_filter = ('status','author')
# admin.site.register(News,NewsAdmin)