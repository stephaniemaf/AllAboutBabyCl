from django.contrib import admin
from .models import Post, Comment, Recipes
from django_summernote.admin import SummernoteModelAdmin


# use summernotefield for the blog content textfield
# @ decorater will register post model and post admin class with admin site

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'pub_date')
    list_display = ('title', 'slug', 'status', 'pub_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'pub_date')
    list_display = ('name', 'body', 'approved', 'pub_date', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Recipes)
class RecipesAdmin(SummernoteModelAdmin):
    list_filter = ('status','ingredients', 'pub_date')
    list_display = ('title', 'ingredients','status','pub_date')
    search_fields = ('title', 'instructions')
    summernote_fields = ('instructions')

