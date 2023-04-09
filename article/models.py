from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
