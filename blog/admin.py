from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# use summernotefield for the blog content textfield
# @ decorater will register post model and post admin class with admin site

@admin.register(Post())
class PostAdmin(SummernoteModelAdmin):
    summernote_fields("content")
