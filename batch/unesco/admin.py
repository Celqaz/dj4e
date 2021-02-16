from django.contrib import admin
from .models import Site, Category, State, Region, Iso


# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    # list_display = ('name', 'year','category', 'state', 'region', 'iso')
    # list_display = ('name', 'category', 'state', 'region', 'iso')
    list_display = ('name', 'year',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Iso)
class IsoAdmin(admin.ModelAdmin):
    pass
