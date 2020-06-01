"""dairy_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_dairy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/', views.accountSignup, name='accountSignup'),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('morning_all_customer/', views.morning_all_customer, name='morning_all_customer'),
    path('evening_all_customer/', views.evening_all_customer, name='evening_all_customer'),
    path('customer_ledger/<pk>', views.customer_ledger, name='customer_ledger'),
    path('customer_ledger_save/', views.customer_ledger_save, name='customer_ledger_save'),
    path('customer_ledger_delete/', views.customer_ledger_delete, name='customer_ledger_delete'),
    path('customer_page/', views.customer_page, name='customer_page'),
    
]
if settings.DEBUG == True or settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
