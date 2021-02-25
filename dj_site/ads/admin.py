from django.contrib import admin
from .models import Ad


# Register your models here.
@admin.register(Ad)
class AdClass(admin.ModelAdmin):
    list_display = ('title', 'price', 'text', 'owner', 'created_at')
    exclude = ('content_type', 'picture')
#     exclude = ('content_type', 'picture')

# class AdAdmin(admin.ModelAdmin):
#     exclude = ('content_type', 'picture')
#
#
# admin.site.register(Ad, AdAdmin)
