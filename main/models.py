from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/category/%Y/%m/%d', verbose_name='Фото')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/category/products/%Y/%m/%d', verbose_name='Фото', blank=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['name']
