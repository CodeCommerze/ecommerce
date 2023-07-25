from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from account.models import User

class Categories(models.Model):
    icon = models.FileField(upload_to='categorY_icons' , null=True ,blank=True)
    image = models.FileField(upload_to='categorY_images' , null=True , blank=True)
    total_sales = models.BigIntegerField(null=True , blank=True , default=0)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , blank=True , null= True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self ,*args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Categories, on_delete= models.CASCADE, related_name = 'sud_category')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255 , null=True , blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Color(models.Model):
    code = models.CharField(max_length=255 , help_text="Enter The HexaCode")
    color_name = models.CharField(max_length=255  , null= True , blank=True)
    price = models.IntegerField(null=True ,blank= True , default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.color_name

class Size(models.Model):
    code = models.CharField(max_length=255 , help_text= "exmp:S , L , XL  ")
    Size_name = models.CharField(max_length=255 ,   null= True , blank=True)
    price = models.IntegerField(null=True ,blank= True , default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.Size_name
        


# product models
class Product(models.Model):
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(SubCategory , on_delete= models.CASCADE , related_name= 'Category')
    title = models.CharField(max_length=2555)
    slug = models.CharField(max_length=255 , null=True , blank=True)
    price = models.IntegerField()
    old_price = models.IntegerField()
    short_description = models.TextField()
    sku = models.CharField(max_length=255 , blank=True, null=True , default="")
    description = RichTextField()
    sold = models.BigIntegerField(null=True , blank=True ,default=0)
    quantity = models.BigIntegerField(null=True, blank=True)
    created = models.DateField(auto_now=True)

    

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_discount_parcent(self):
        discount = int(((self.old_price - self.price)/self.old_price)*100)
        return discount
    
    def get_status(self):
        status = 'In Stock'
        if self.quantity <=0:
            status = "Out of Stock"
        return status
    
    
# product image gallery models
class Prodcut_Gallery(models.Model):
    product = models.ForeignKey(Product,related_name='product_gallery' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/prioduct_gallery_image' , null=True , blank=True)


    def __str__(self):
        return self.product.title
    



# Wish List Model
class WishList(models.Model):
    user = models.ForeignKey(User , related_name= 'wistlist' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='wishlist_product', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    

    






    
