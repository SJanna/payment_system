from django.urls import include, path
from rest_framework import routers
from .views import TransactionLogViewSet

router = routers.DefaultRouter()
router.register(r'transaction-logs', TransactionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]