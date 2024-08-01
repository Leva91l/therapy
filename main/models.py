from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/category/%Y/%m/%d')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/category/products/%Y/%m/%d')
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product', kwargs={'prod_id': self.pk})
