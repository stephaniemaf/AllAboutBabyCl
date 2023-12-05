from . import views
from django.urls import path

# connecting views to url

urlpatterns = [
    path('', views.PostList.as_view(), name='home')
         ]
