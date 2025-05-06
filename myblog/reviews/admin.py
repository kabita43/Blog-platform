from django.contrib import admin
from .models import WatchList , Review

# Register your models here.

class WatchListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'storyline')
admin.site.register(WatchList,WatchListAdmin)
admin.site.register(Review)
