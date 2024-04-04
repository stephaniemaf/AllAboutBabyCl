from . import views
from django.urls import path
from .views import UpdateComment, CreateRecipe

# connecting views to url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipe/', views.RecipeList.as_view(), name='recipe'),
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe_add_user/', views.CreateRecipe.as_view(), name='recipe_add_user'),
    path('comment_update_form/<int:pk>/', views.UpdateComment.as_view(), name='comment_update_form'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('recipe/like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
