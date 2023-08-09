from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'address', 'postal_code', 'phone_number')
    search_fields = ('username', 'phone_number')

admin.site.register(Customer, CustomerAdmin)