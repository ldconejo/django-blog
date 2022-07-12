from django.contrib import admin

# Register your models here.
from blogging.models import Post

admin.site.register(Post)