from django.contrib import admin
from .models import Catalog, CatalogCategory, Product, ProductAttribute, ProductDetail
# Register your models here.

admin.site.register(CatalogCategory)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Catalog)
admin.site.register(ProductAttribute)
