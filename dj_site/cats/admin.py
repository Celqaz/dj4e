from django.contrib import admin
from .models import Cat, Breed
# Register your models here.
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass