from django.urls import include, path
from rest_framework import routers
from .views import PaymentMethodViewSet

router = routers.DefaultRouter()
router.register(r'payment-methods', PaymentMethodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]