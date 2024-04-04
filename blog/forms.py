from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeAddUser(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title','author','featured_image','ingredients','instructions',)

