from .models import Comment, RecipeComment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('body',)

class RecipeAddUser(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title','author','featured_image','ingredients','instructions',)

