from django.contrib import admin
from .models import Blog, Category


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "slug")
    list_editable = ("is_home", "is_active")
    search_fields = ("title", "description")
    readonly_fields = ("slug",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    readonly_fields = ("slug",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
