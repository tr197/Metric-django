from django.contrib import admin
from product.models import (
    Category, CategorySub, 
    Product, ProductImages,
    ProductOptions, ProductComments
)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)



class ProductImageInLine(admin.TabularInline):
    model = ProductImages
    extra = 0
    

class ProductOptionInLine(admin.TabularInline):
    model = ProductOptions
    extra = 0


class ProductCommentInLine(admin.TabularInline):
    model = ProductComments
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    inlines = [ProductImageInLine, ProductOptionInLine, ProductCommentInLine]
    ordering= ['category', 'slug',]
    list_filter = ['category',]
    search_fields = ['slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategorySub, CategoryAdmin)
admin.site.register(Product, ProductAdmin)