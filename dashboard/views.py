from django.shortcuts import get_object_or_404 ,redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login  , authenticate
from django.views.generic import  *
from account.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.forms.models import model_to_dict
#Shop MOdel 
from shop.models import *
# froms
from dashboard.forms import *


#Admin Authentication parts
def AdminLoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        context = {}
        if user is not None:
            if user.role =='Admin' and user.is_verified:
                login(request, user)
                return redirect('admin_dashboard')
            elif user.role =='Coustomer':
                login(request, user)
                return redirect('dashboard')
            elif user.role =='Vendor':
                login(request, user)
                return HttpResponse("Welcome you are login as a Vendor")
            
        context['error'] = 'Invalid username or password'
        return render(request, 'dashboard/login.html', context)         
    return render(request, 'dashboard/login.html')

# Index Dahsboard View
class DashboardView( LoginRequiredMixin,TemplateView):
    template_name ='dashboard/index.html'
    login_url ='admin_login'
    success_url = 'admin_dashboard'


    def dispatch(self  , *args, **kwargs):
      
        if self.request.user.is_authenticated:
            if self.request.user.role == 'Admin':
                return super().dispatch(  *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
    


# category views

class CategoryView(LoginRequiredMixin, ListView  ):
    template_name = 'dashboard/main-category.html'
    login_url = 'admin_login'
    model = Categories
    context_object_name = 'categories'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
        
    def update_category_json_data(self ,slug):
         category = get_object_or_404(Categories, slug=slug)
         if category:
                category_data = {
                    "id": category.id,
                    "name": category.name,
                    "slug": category.slug,
                   
                }
                return JsonResponse({"category": category_data})
         else:
                return JsonResponse({"category": False})
         
    # 
    def delete_category(self, slug):
        quryset = get_object_or_404(Categories , slug=slug)
        if quryset:
            quryset.delete()
            return redirect('category')
        else :
            return messages.warning("Category not found")
    
   
class CategoryCreateView(LoginRequiredMixin , CreateView):
    template_name = 'dashboard/main-category.html'
    login_url = 'admin_login'
    model = Categories
    form_class = Category_form
    success_url = 'category'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
        
    def form_valid(self , form):
        messages.success(self.request,"Category Created Successfully")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class CategoryUpdate(UpdateView):
    form_class = Category_form
    model = Categories
    success_url = reverse_lazy("category")
    slug_field = 'slug'


    
#subcategory Views
class SubcategoryView(LoginRequiredMixin, CreateView):
    model = SubCategory
    form_class = subCategoryForm
    template_name = 'dashboard/sub-category.html'
    login_url = 'admin_login'
    success_url = 'add-subcategory' 
   


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.all()
        context['subCategory'] = SubCategory.objects.all()
        return context
    
    
    def form_invalid(self, form):
        messages.success("Sub Category Created ")
        return super().form_invalid(form)
    

    def form_valid(self , form):
        print(form.errors)
        return super().form_valid(form)
    
    # custom functions for subcategory deletion
    def delete_subcategory(self , slug):
        queryset = get_object_or_404(SubCategory, slug=slug)
        if queryset:
            queryset.delete()
            return redirect('add-subcategory')
        else:
            return messages.warning('subcategory not found')
        
    # custom functions for subcategory json generation
    def get_subcategory_json(self, slug):
        query = get_object_or_404(SubCategory, slug=slug)
        data = {
            'name': query.title,
            'slug': query.slug,
            'category': query.category.id
        }
        return JsonResponse(data)

# All Product  Related View
class CreaeProductView(CreateView):
    model = Product
    template_name = 'dashboard/product-add.html'
    form_class = Product_Form
    success_url = 'add-product'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
        
class ProductList(ListView):
    model = Product
    context_object_name ='products'
    template_name = 'dashboard/product-list.html'
    queryset = Product.objects.filter(quantity__gt=0)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
    
    def product_delte(self  , slug):
        if self.user.role == 'Admin':
            queryset = get_object_or_404(Product , slug=slug)
            queryset.delete()
            return redirect('product-list') 
        else :
            return redirect('dashboard')
           

     
        
class StockOutProductVIew(ListView):
    model = Product
    template_name = 'dashboard/stockout-product.html'
    queryset = Product.objects.filter(quantity = 0)
    context_object_name = 'so_products'

    # befor runing cheking if admin or not
    def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.role == 'Admin':
                    return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
      
            return redirect('admin_login')
   


class ProductDetailView(DetailView):
    model = Product
    template_name = 'dashboard/product-detail.html'
    slug_field = 'slug'
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')

 
class ProductUpdateView(UpdateView):
    model = Product
    form_class = Product_Form
    success_url = reverse_lazy('product-list')
    slug_field = 'slug'
    template_name = 'dashboard/product-update.html'
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')




#UserList View
class UserLitView(LoginRequiredMixin ,ListView):
    model = CustomerProfile
    template_name = 'dashboard/user-list.html'
    context_object_name = 'users'
    login_url = 'admin_login'


    

    def dispatch(self  , *args, **kwargs):
      
        if self.request.user.is_authenticated:
            if self.request.user.role == 'Admin':
                return super().dispatch(  *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')
class UserPrfileView(LoginRequiredMixin , DetailView):
    template_name = 'dashboard/user-profile.html'
    model = CustomerProfile
    context_object_name = 'customer'
    login_url = 'admin_login'


# wishlist views
class WishListVIew( LoginRequiredMixin,ListView):
    template_name = 'dashboard/wishlist.html'
    model = WishList
    context_object_name = 'wishlists'
    login_url = 'admin_login'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'Admin':
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('admin_login')





    
        




    



    

