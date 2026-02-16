from django.contrib import admin
from .models import ContactSubmission, APIRequest

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(APIRequest)
class APIRequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'use_case', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('company_name', 'email', 'use_case', 'message')
    list_editable = ('is_approved',)
    readonly_fields = ('created_at',)

# Global Admin Customization
admin.site.site_header = "پنل مدیریت Esearch"
admin.site.site_title = "Esearch AdminPanel"
# admin.site.index_title = "به پنل مدیریت خوش آمدید"
