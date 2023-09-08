from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    created = models.DateTimeField()
    category = models.ForeignKey(to=Category, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created']

    def __str__(self):
        return self.slug
