from django.urls import path
from account.views import *
from django.contrib.auth.views  import LogoutView
urlpatterns = [
    path('register' , CustomerRegistration , name ='customer_register'),
    path('login' , login_user , name = 'login'),
    path('dashboard' , DashboardView.as_view(), name = 'dashboard'),
    path('updat_data' , DashboardView.update_data , name = 'data_update'),
    path('logout' , LogoutView.as_view(next_page="login") , name="logout"),
    # this is vendor url sections
    path('vendor-apply' , VendorRequest.as_view(),name = 'vendor_apply' )
]