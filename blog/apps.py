from django.apps import AppConfig
from django.db.models.signals import post_migrate


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def content(self):
        from django.contrib.contenttypes.models import ContentType
        from .models import Post, Recipe

        post_migrate.connect(self.create_content_types, sender=self)
    
    def create_content_types(self, sender, **kwargs):
        ContentType.objects.get_or_create(model='post', app_label='blog', defaults={'name': 'Post'})
        ContentType.objects.get_or_create(model='recipe', app_label='blog', defaults={'name': 'Recipe'})