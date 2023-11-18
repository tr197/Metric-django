import uuid
from django.db import models



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
        return f'{self.parent_category.name[:70]} > {self.name[:200]}'


class Product(GeneralInfo):
    category = models.ForeignKey(CategoryBase, related_name='products',
                                 on_delete=models.CASCADE,
                                 null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/product/main')
    
    class Meta:
        db_table = 'product'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product/other')

    class Meta:
        db_table = 'product_image'