from . import views
from django.urls import path

# connecting views to url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipes/', views.PostList.as_view(), name='recipe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
