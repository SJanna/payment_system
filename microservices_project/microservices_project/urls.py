"""
URL configuration for microservices_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transaction_capture.urls')),
    path('', include('balance_validation.urls')),
    path('', include('credit_card_validation.urls')),
    path('', include('payment_methods.urls')),
    path('', include('transaction_processing.urls')),
    path('', include('balance_inquiry.urls')),
    path('', include('user_interface.urls')),
    path('', include('transaction_logging.urls')),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]