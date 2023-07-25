from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import UserManager 
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save 
from django.dispatch import receiver




class User(AbstractUser):
   class Role(models.TextChoices):
      Admin = 'Admin',"Admin"
      Coustomer = 'Coustomer',"Coustomer"
      Vendor = 'Vendor',"Vendor"  
   email = models.EmailField(verbose_name = 'email')
   is_verified = models.BooleanField(default=False , verbose_name='Is Verified')
   role = models.CharField(max_length=255, verbose_name='Role' , choices=Role.choices )
   created = models.DateField(auto_now_add=True)
   base_role = Role.Admin

   objects = UserManager()

   def save(self, *args, **kwargs):
      if not self.pk:
         self.role = self.base_role
      return super().save(*args, **kwargs)

   def __str__(self):
      return self.username




# customer proxy model and manager

# manager
class CustomerManager(BaseUserManager):
    def get_queryset(self ,*args, **kwargs) :
        reasult =  super().get_queryset(*args, **kwargs)
        return reasult.filter(role=User.Role.Coustomer)
    
   
    def create_user(self, email, password=None, **extra_fields):
        if  not email :
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

#proxy model
class Coustomer(User):
   base_role = User.Role.Coustomer
   objects = CustomerManager()
   class Meta:
      proxy = True




# # Vendor proxy model and manager

# manager
class VendorManager(BaseUserManager):
    def get_queryset(self ,*args, **kwargs) :
        reasult =  super().get_queryset(*args, **kwargs)
        return reasult.filter(role = User.Role.Vendor)
    
   
    def create_user(self, email, password=None, **extra_fields):
        if  not email :
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

#proxy model
class Vendor(User):
   base_role = User.Role.Vendor
   objects = VendorManager()
   class Meta:
      proxy = True


# Customer Profile Model
class CustomerProfile(models.Model):
   user = models.OneToOneField(Coustomer, on_delete=models.CASCADE , related_name='profile' , null=True ,blank=True)
   cover_image = models.ImageField(upload_to='customer/cover' , blank=True ,null=True)
   email_second = models.EmailField(null=True , blank=True)
   image = models.ImageField(upload_to='coustomer_profile' , null=True ,blank=True)
   first_name = models.CharField(max_length= 255 , verbose_name='First Name' , blank=True , null=True)
   last_name = models.CharField(max_length= 255 , verbose_name='Last Name' , blank= True, null=True)
   phone = models.CharField(max_length= 255 , verbose_name='Phone Number' , blank= True, null=True)
   phone_second = models.CharField(max_length= 255 , verbose_name='Phone Numbr 2', blank= True, null=True)
   address  = models.TextField(blank=True , null=True)
   postcode = models.CharField(max_length= 255 , verbose_name='Post Code' , blank= True, null=True)
   
   def __str__(self):
      return self.user.username
   
   def getImage(self):
      image_url = ""
      if self.image:
         image_url = self.image.url
      else:
         image_url = "https://cdn.iconscout.com/icon/free/png-256/free-avatar-370-456322.png?f=webp"
      return image_url


# Vendor Profile Model
class VendorProfile(models.Model):
   user = models.OneToOneField(Vendor, on_delete=models.CASCADE , related_name='vendor_profile')
   full_name = models.CharField(max_length= 255 , verbose_name='Full Name' , blank=True , null=True)

   def __str__(self):
      return self.user.username
   
# vendor Request Model
class VendorApply(models.Model):
   image = models.ImageField(upload_to='vendor_request')
   nid_picture  = models.ImageField(upload_to="vendor_nid_picture")
   frist_name = models.CharField(max_length=255 )
   last_name = models.CharField(max_length=255 )
   mobile =  models.CharField(max_length=50)
   email = models.EmailField()
   company_name = models.CharField(max_length=255)
   registere_number = models.CharField(max_length=255)
   address = models.TextField()
   shop_address = models.TextField()
   created = models.DateField(auto_now_add=True)
   def __str__(self):
      return self.frist_name
   
   
   
   





# signals of vendor Profile

@receiver(post_save, sender=Vendor)
def create_vendor_profile(sender, instance, created, **kwargs):
   if created:
      VendorProfile.objects.create(user=instance)

@receiver(post_save, sender=Vendor)
def save_vendor_profile(sender, instance, **kwargs):
   instance.vendor_profile.save()


# signals for Customer

@receiver(post_save, sender=Coustomer)
def create_customer_profile(sender, instance, created, **kwargs):
   if created:
      CustomerProfile.objects.create(user=instance)

@receiver(post_save, sender=Coustomer)
def save_customer_profile(sender, instance, **kwargs):
   instance.profile.save()

   