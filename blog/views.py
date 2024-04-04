from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.contenttypes.models import ContentType
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .models import Post, Recipe, Comment
from .forms import CommentForm, RecipeAddUser, CommentUpdateForm, DeleteCommentForm



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

class UpdateComment(UpdateView,FormMixin):
    model = Comment
    form_class = CommentUpdateForm
    template_name = "comment_update_form.html"
    def get_success_url(self):
        post_slug = self.object.post.slug
        return reverse_lazy('post_detail', kwargs={'slug': post_slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteComment(DeleteView,FormMixin):
    model = Comment
    form_class = DeleteCommentForm
    template_name = "delete_comment_form.html"
    success_url = reverse_lazy('post_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateRecipe(CreateView,FormMixin):
    model = Recipe
    form_class = RecipeAddUser
    template_name = "recipe_add_user.html"
    success_url = reverse_lazy('recipe') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Success, Please await admin approval')
        return super().form_valid(form)


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
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.content_object = post
            content_type = ContentType.objects.get(app_label="blog", model="post")
            comment.content_type = content_type
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

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
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
                "comment_form": CommentForm()
            },
        )

        
    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-pub_date")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.content_object = recipe
            content_type = ContentType.objects.get(app_label="blog", model="recipe")
            comment.content_type = content_type
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
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


class RecipeLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))




