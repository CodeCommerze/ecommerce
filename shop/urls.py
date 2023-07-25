from django.urls import path
from shop.views import *

urlpatterns = [
    path('' , IndexView.as_view() , name = 'index'),
    

]
