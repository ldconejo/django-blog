from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoryInPostInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInPostInline,)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryInPostInline,)
    exclude = ('posts', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)