from unicodedata import name
from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

class PicturesConfig(AppConfig):
    name='pictures'
