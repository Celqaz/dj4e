from django.contrib import admin
from .models import Make, Auto


# Register your models here.
@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'mileage', 'comments','make')
