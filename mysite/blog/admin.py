from django.contrib import admin
from .models import Post


# Register your models here.
# The @admin.register() decorator performs the same function as the admin.site.register() function,
# registering the ModelAdmin class that it decorates.
# admin.site.register(Post)
@admin.register(Post)
# You are telling the Django administration site that your model is registered in
# the site using a custom class that inherits from ModelAdmin.

class PostAdmin(admin.ModelAdmin):
    # The *list_display* attribute allows you to set the fields of your model that you
    # want to display on the administration object list page.
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # 预定义字段
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
