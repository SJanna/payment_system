from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class BalanceValidationView(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        
        if amount is not None and amount > 0:
            # Perform balance validation logic
            # Example: Check balance against available funds in accounts or credit cards
            
            # If balance is sufficient
            return Response({'message': 'Balance is valid'}, status=status.HTTP_200_OK)
        else:
            # If balance is insufficient or invalid
            return Response({'message': 'Insufficient balance or invalid amount'}, status=status.HTTP_400_BAD_REQUEST)