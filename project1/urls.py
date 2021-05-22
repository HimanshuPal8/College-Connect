"""project1 URL Configuration
"""
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('',include('testing.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
]
