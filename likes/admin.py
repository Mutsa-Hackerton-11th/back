from django.contrib import admin
from .models import Liked

class LikedAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')

admin.site.register(Liked, LikedAdmin)