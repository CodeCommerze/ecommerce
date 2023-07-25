from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import *
from shop.models import *

class IndexView(ListView):
    model = Product
    template_name = 'frontend/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        print(context)
        return context
