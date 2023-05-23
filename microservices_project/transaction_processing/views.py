from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionProcessingView(APIView):
    def post(self, request):
        transaction_id = request.data.get('transaction_id')
        
        if transaction_id is not None:
            # Perform transaction processing logic
            # Example: Deduct amount from the customer's account or credit card
            
            # If transaction processing is successful
            return Response({'message': 'Transaction processed successfully'}, status=status.HTTP_200_OK)
        else:
            # If transaction processing fails
            return Response({'message': 'Transaction processing failed'}, status=status.HTTP_400_BAD_REQUEST)
