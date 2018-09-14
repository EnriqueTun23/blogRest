from django.contrib import admin
from .models import post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "update", "publish"]
    list_filter = ["publish"]
    search_fields = ["title"]
    class Meta:
        model = post

admin.site.register(post, PostModelAdmin)
