import uuid
from django.core.validators import MinValueValidator
from django.core.cache import cache

from django.db import models
from django.db.models import Min
from django.utils.text import slugify
from app.settings import APP_URL
from shop.models import Platform
from product.constants import DataKey

class GeneralInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:200]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CategoryBase(GeneralInfo):

    class Meta:
        db_table = 'category_base'
        
    def save(self, *args, **kwargs):
        cache.delete(DataKey.CATEGORY_LIST.value)
        return super().save(*args, **kwargs)


class Category(CategoryBase):

    class Meta:
        db_table = 'category'


class CategorySub(CategoryBase):

    parent = models.ForeignKey(Category, related_name='children',
                                        on_delete=models.CASCADE,
                                        null=False, blank=False,)

    class Meta:
        db_table = 'category_sub'

    def __str__(self) -> str:
        return f'{self.parent.name[:70]} > {self.name[:200]}'


class Product(GeneralInfo):
    category = models.ForeignKey(CategoryBase, related_name='products',
                                 on_delete=models.CASCADE,
                                 null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/product/main')
    price = models.IntegerField(null=True, blank=True, default=999999999)
    
    class Meta:
        db_table = 'product'

    def main_image_url(self):
        return APP_URL + self.image.url

    def __other_image_urls(self):
        return [
            f'{APP_URL}{item.image.url}'
            for item 
            in self.other_images.all()
            ]
        
    def image_urls(self):
        return [self.main_image_url()] + self.__other_image_urls()
        
    def calculate_price(self):
        options = self.options.all()
        if len(options) == 0:
            return self.price
        min_price = options.aggregate(min_price=Min('price'))
        return min_price['min_price']


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product/other')

    class Meta:
        db_table = 'product_image'
        
        

class ProductOptions(models.Model):
    product = models.ForeignKey(Product, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True)
    # description = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=999999999)
    sale_count = models.IntegerField(null=False, blank=True, default=0, validators=[MinValueValidator(0)])
    platform = models.ForeignKey(Platform, null=True, blank=False, on_delete=models.PROTECT)
    link = models.CharField(null=False, blank=False, default='/')

    class Meta:
        db_table = 'product_option'
        
        
class ProductComments(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    
    class Meta:
        db_table = 'product_comment'
        
    def __str__(self) -> str:
        return f'{self.username} -> {self.content[:30]}'