from django.contrib import admin
from .models import Lang, Book, Instance


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'lang',)
    search_fields = ('title', 'isbn')
    list_filter = ('lang', )


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back',)
