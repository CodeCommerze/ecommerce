from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include 

urlpatterns = [
    path('old_admin/', admin.site.urls),
    path('' , include('shop.urls') , name ='home'),
    path('account/' , include('account.urls') , name = 'account'),
    path('admin/' , include('dashboard.urls') , name ='admin_dashboard'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL  , document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

