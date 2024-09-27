from django.db import models


class Taggable(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Тэг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField(Taggable, through='ArticlesTags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class ArticlesTags(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles_tags')
    tags = models.ForeignKey(Taggable, on_delete=models.CASCADE, related_name='articles_tags')
    is_main = models.BooleanField()

    class Meta:
        ordering = ['-is_main']
