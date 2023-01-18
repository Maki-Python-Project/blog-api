from django.db import models

from articles.models import Article
from users.models import User


class Comment(models.Model):
    text = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments', null=True
    )
    published = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.text}; author: {self.customer}'
