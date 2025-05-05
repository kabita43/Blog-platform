from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display=('title','slug','published','created')
    # prepopulated_fields={'slug':('title',)}
    # list_filter=('published','created')
    search_fields=('title','body')
