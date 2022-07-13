from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # DEDICATED TO API VIEWS
    path('api/', include('product.api.urls')),

    # DEDICATED TO PRODUCT
    path('', include('product.urls')),
    path('product/', include('product.urls')),

    # DEDICATED TO ORDER
    # path('order/', include('order.urls')),
]
