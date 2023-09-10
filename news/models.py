from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-only', args=[self.slug])

class Article(models.Model):
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(to=Category, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('full-article', args = [self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

