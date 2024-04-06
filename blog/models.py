from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType



STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='post_likes', blank=True)
    

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    recipe = models.ForeignKey(
        'blog.Recipe', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")  
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["pub_date"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.user}"

    
# Custom model


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True,)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)

    class Meta:
        ordering = ["pub_date"]
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)

        
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Subscribe(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email