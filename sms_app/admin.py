# sms_app/admin.py
from django.contrib import admin
from .models import Student, Category, Achievement

class StudentAdmin(admin.ModelAdmin):
    # These strings MUST match the field names in models.py
    list_display = ('name', 'register_number', 'course', 'status') 
    search_fields = ('name', 'register_number') 
    list_filter = ('course', 'status')

admin.site.register(Student, StudentAdmin)
admin.site.register(Category)
admin.site.register(Achievement)