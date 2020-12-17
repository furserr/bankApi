from rest_framework import serializers
from .models import Account, Customer, Transfer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','url', 'name')

class AccountSerializer(serializers.ModelSerializer):
    #customer = CustomerSerializer(read_only=False)
    class Meta:
        model = Account
        fields = ('id','url', 'balance', 'customer')

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('id','url', 'sender', 'receiver', 'balance')