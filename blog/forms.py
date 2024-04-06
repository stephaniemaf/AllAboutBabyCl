from .models import Comment, Recipe, Subscribe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class DeleteCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ()

class RecipeAddUser(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title','author','featured_image','ingredients','instructions',)

class Subscriber(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('first_name','last_name','email','phone_number',)

