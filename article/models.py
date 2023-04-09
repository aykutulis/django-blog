from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
