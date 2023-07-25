from django.contrib import admin

from .models import *

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'image', 'name', 'slug', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'slug')       
    list_filter = ('category',)
    search_fields = ('slug',)


class Product_Gallery_Admin(admin.TabularInline):
    model = Prodcut_Gallery
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'category',
        'title',
        'slug',
        'price',
        'old_price',
        'short_description',
        'description',
        'quantity',
        'created',
    )
    list_filter = ('category', 'created')
    search_fields = ('slug',)
    inlines = [Product_Gallery_Admin]

@admin.register(WishList)
class WishListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created')      
    list_filter = ('user', 'product', 'created')
