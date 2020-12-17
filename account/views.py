from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Customer, Account, Transfer
from .serializers import CustomerSerializer, AccountSerializer, TransferSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransferView(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

@api_view(['GET'])
def TransferHistory(request, id):
    if request.method == 'GET':
        account = get_object_or_404(Account, id=id)
        transfers = Transfer.objects.all()
        history = transfers.filter(sender=account) | transfers.filter(receiver=account)
        if history:
            serializer = TransferSerializer(history, many=True,context={'request':request})
            return Response(serializer.data)
        else:
            raise ValidationError({'Not Found': "This account has no transfer history"}, code=400)
