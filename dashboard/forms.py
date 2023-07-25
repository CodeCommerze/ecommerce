from shop.models import *
from django import forms



class Category_form(forms.ModelForm):
    class Meta:
        model = Categories
        fields= ['image' , 'icon' , 'name' ,'slug']



class subCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'title', 'slug']


class Product_Form(forms.ModelForm):
    gallery_images = forms.ImageField(required=False)
    class Meta:  
        model = Product
        fields = "__all__"

    def save(self, commit=True):
        product = super().save(commit=commit)
      
        gallery_images = self.files.getlist("gallery_images")
        print(gallery_images)
        if gallery_images:
         for image_in in gallery_images:
           try:
             Prodcut_Gallery.objects.create(product=product, image=image_in)
           except Exception as e:
             print (e)
        return product
        
