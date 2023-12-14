from .models import Comment, RecipeComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('body',)


