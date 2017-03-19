from datetime import datetime

from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{0}'.format(self.name)


class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='product')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_naira = models.DecimalField(max_digits=9, decimal_places=2)


class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.parent:
            return '{0} {1} {2}'.format(self.catalog.name, self.parent.name, self.name)
        return '{0} {1}'.format(self.catalog.name, self.name)


class ProductDetail(models.Model):
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.product, self.attribute, self.value)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{0}'.format(self.name)
