from django.contrib import admin
from .models import AccountClassification

@admin.register(AccountClassification)
class AccountClassificationAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_code']  
    search_fields = ['account_name', 'account_code'] 
