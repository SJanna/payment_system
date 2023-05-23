from rest_framework import viewsets
from .models import TransactionLog
from .serializers import TransactionLogSerializer

class TransactionLogViewSet(viewsets.ModelViewSet):
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionLogSerializer
