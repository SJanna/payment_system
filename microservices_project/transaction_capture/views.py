# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Transaction
from .serializers import TransactionSerializer
import requests

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def process_transaction(self, request, pk=None):
        transaction = self.get_object()
        
        # Validating balance using the Microservice of Balance Validation
        balance_validation_url = 'http://balance_validation_service_url/validate-balance/'
        response = requests.post(balance_validation_url, data={'amount': transaction.amount})
        if response.status_code == 200:
            # Balance validation successful, proceed with transaction processing
            transaction.save()

            # Processing transaction using the Transaction Processing Microservice
            transaction_processing_url = 'http://transaction_processing_service_url/process-transaction/'
            response = requests.post(transaction_processing_url, data={'transaction_id': transaction.pk})
            if response.status_code == 200:
                # Transaction processing successful
                return Response({'message': 'Transaction processed successfully'})
            else:
                # Transaction processing failed
                return Response({'message': 'Transaction processing failed'})
        else:
            # Balance validation failed
            return Response({'message': 'Insufficient balance'})
