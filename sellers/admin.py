from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('username', 'company_name', 'company_level', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('username', 'company_name', 'phone_number')

admin.site.register(Seller, SellerAdmin)