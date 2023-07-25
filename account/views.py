from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse
from django.views.generic import *
from account.models import * 
from account.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from account.decoretors import redirect_authenticated_user
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import *

# Coustomer Register fuction
@redirect_authenticated_user
def CustomerRegistration(request):
   if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    if Coustomer.objects.filter(username__iexact=username):
         messages.warning(request, 'Username already exists')
         return redirect('customer_register')
    if Coustomer.objects.filter(email__iexact=email):
        messages.warning(request, 'Email already exists')
        return redirect('customer_register')
    customer = Coustomer.objects.create_user(username = username,  email = email , password=password)
    if customer:
        return redirect('login')         
   return render(request, 'frontend/account/customer.html')


# Coustmer login Part 
@redirect_authenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user.role)
        if user is not None :
            if user.role =='Admin' and user.is_verified:
                login(request, user)
                return redirect('admin_dashboard')
            elif user.role =='Coustomer':
                login(request, user)
                return redirect('dashboard')
            elif user.role =='Vendor':
                login(request, user)
                return HttpResponse("Welcome you are login as a Vendor")
        
    
    return render(request, 'frontend/account/login.html')
   


# Ciustomer Part 
class DashboardView( LoginRequiredMixin,TemplateView , RedirectView):
        template_name = 'frontend/account/user-profile.html'
        login_url = 'login'

        
        def dispatch(self , *args, **kwargs):
            if self.request.user.role == 'Coustomer':
                return super().dispatch(*args, **kwargs)
            elif self.request.user.role == 'Admin':
                return redirect("admin_dashboard")
            
            return redirect('login')

        def get_context_data(self, **kwargs) :
                context = super().get_context_data(**kwargs)
                context['profile_data'] = CustomerProfile.objects.get(user = self.request.user)
                return context
        

        def update_data(self ):
            form = CustomerProfileForm()
            user = get_object_or_404(User, username = self.user)
            print(self.FILES)
            if self.method == 'POST':
                form = CustomerProfileForm(self.POST , self.FILES , instance= user.profile)
                if form.is_valid():
                    form.save()
                    return redirect('dashboard')


class vendorView(LoginRequiredMixin ,TemplateView ):
   template_name = 'forntend/account/vendor-profile.html'
   login_url = 'login'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['vendor_profile'] =  VendorProfile.objects.get(user = self.user)
       return context


class VendorRequest(CreateView):
    template_name = "frontend/account/vendor.html"
    form_class = VendorRequestForm
    model = VendorApply
    success_url = 'vendor-apply'



    

