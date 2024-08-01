from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/category/%Y/%m/%d', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/category/products/%Y/%m/%d')
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product', kwargs={'prod_id': self.pk})
