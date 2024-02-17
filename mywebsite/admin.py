from django.contrib import admin
from mywebsite.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'message',) 
  