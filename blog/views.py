from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).orderby("-pub_date")
    template_name = "index.html"
    paginate_by = 6
