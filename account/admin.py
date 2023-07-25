from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
    
        'username',
        'email',
        'is_verified',
        'role',
        'created',
    )
    list_filter = (
        'is_superuser',
        'is_verified',
        'created',
        'role'
    )
    search_fields = ('username', 'email')
    
@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name' , 'phone')
 


@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user' ,)
    

@admin.register(VendorApply)
class VendorApplyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'nid_picture',
        'frist_name',
        'last_name',
        'mobile',
        'company_name',
        'registere_number',
        'address',
        'shop_address',
    )