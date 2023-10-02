from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = ['first_name', 'last_name', 'phone', 'email', 'category']
    search_fields = ['first_name']
    ordering =['id']
    list_per_page = 50
    list_max_show_all = 50
    list_display_links = ['first_name', 'last_name']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['name']
    search_fields = ['name']
    ordering =['id']
    list_per_page = 50
    list_max_show_all = 50
    list_display_links = ['name']