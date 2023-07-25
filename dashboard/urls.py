from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('login' , AdminLoginView , name= 'admin_login'),
    path('', DashboardView.as_view() , name = "admin_dashboard"),
    # category & subcategory routes
    path('category', CategoryView.as_view() , name ='category'),
    path('add-category', CategoryCreateView.as_view() , name='add-category'),
    path('catagory/<slug:slug>/json' , CategoryView.update_category_json_data , name= 'category-json'),
    path('category/<slug:slug>/update' , CategoryUpdate.as_view() , name='category-update'),
    path('category/<slug:slug>/delete' , CategoryView.delete_category , name = 'category-delete'),
    # subcategory routes
     path('add-subcategory',SubcategoryView.as_view() , name ='add-subcategory'),
     path('subcategory/<slug:slug>/delete' , SubcategoryView.delete_subcategory , name = 'delete-subcategory'),
     path('subcategory/<slug:slug>/json',SubcategoryView.get_subcategory_json , name = 'get-subcategory-json'),
    #  Product routes
    path('add-product', CreaeProductView.as_view() , name= 'add-product'),
    path('product-list', ProductList.as_view() , name ='product-list'),
    path('product-details/<str:slug>', ProductDetailView.as_view() , name = 'product-details'),
    path('stockout-product', StockOutProductVIew.as_view() , name = 'stock-out-product'),
    path('product/<slug:slug>/delete/', ProductList.product_delte, name='product-delete'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),

    # User Routes
    path('user-list' , UserLitView.as_view(), name= 'user_list'),
    path('user-profile/<str:pk>' , UserPrfileView.as_view() , name= 'user-profile'),
    # wishlist routes
    path('wishlist' , WishListVIew.as_view() , name= 'wishlist'),
    
]

