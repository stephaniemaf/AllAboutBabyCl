from . import views
from django.urls import path
from .views import UpdateComment

# connecting views to url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipe/', views.RecipeList.as_view(), name='recipe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('recipe/<int:id>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('recipe/like/<int:id>', views.RecipeLike.as_view(), name='recipe_like'),
    
    path('comments/<int:pk>/update/', UpdateComment.as_view(), name='comment_update_form'),
]
