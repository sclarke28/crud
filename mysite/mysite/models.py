from turtle import title
from unittest.util import _MAX_LENGTH


class Post(models.Models):
    title = models.CharField(max_length=208)
    author = models.ForiegnKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def _self_(self):
        return self.title
