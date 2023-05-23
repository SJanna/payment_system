from django.urls import include, path
from rest_framework import routers
from .views import CreditCardViewSet

router = routers.DefaultRouter()
router.register(r'credit-cards', CreditCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]