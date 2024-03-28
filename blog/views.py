from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .models import Post
from .forms import CommentForm, RecipeCommentForm
from .models import Recipe
from .models import Comment



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-pub_date")
    template_name = "index.html"
    paginate_by = 6

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-pub_date")
    template_name = "recipe_index.html"
    paginate_by = 6

class UpdateComment(UpdateView):
    model = Comment
    fields = ["body"]
    template_name = "comment_update_form.html"
    success_url = reverse_lazy('post_detail') 

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.post.slug})
    

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-pub_date")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-pub_date")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class RecipeDetail(View):

    def get(self, request, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset)
        comments = recipe.comments.filter(approved=True).order_by("-pub_date")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": RecipeCommentForm()
            },
        )
    
    def post(self, request, id, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, id=id)
        comments = recipe.comments.filter(approved=True).order_by("-pub_date")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = RecipeCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = RecipeCommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": RecipeCommentForm()
            },
        )

class RecipeLike(View):
    
    def post(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[id]))




