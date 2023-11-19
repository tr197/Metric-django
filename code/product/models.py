import uuid
from django.db import models
from django.utils.text import slugify
from app.settings import APP_URL


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

    def other_image_urls(self):
        return [
            f'{APP_URL}{item.image.url}'
            for item 
            in self.other_images.all()
            ]


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product/other')

    class Meta:
        db_table = 'product_image'