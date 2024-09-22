from django.contrib import admin

from .models import AccountTypes

@admin.register(AccountTypes)
class AccountTypesAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_code', 'description', 'financial_statement', 'account_classification']  
    search_fields = ['account_name', 'account_code', 'description', 'financial_statement', 'account_classification'] 