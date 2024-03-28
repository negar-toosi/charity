from django.contrib import admin
from news.models import News, Category, Comments, Newsletter
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author', 'views', 'created_date', 'status', 'published_date')
    list_filter = ('status','author')
    summernote_fields = ('content',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','news', 'created_date', 'approved')
    list_filter = ('news','approved')
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Newsletter)