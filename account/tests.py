from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Account, Transfer

class BankTests(APITestCase):

    def test_status(self):
        url1 = reverse('account:customers-list')
        url2 = reverse('account:accounts-list')
        url3 = reverse('account:transfers-list')
        response1 = self.client.get(url1, format='json')
        response2 = self.client.get(url2, format='json')
        response3 = self.client.get(url3, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

    def create_customer(self):
        data = {
            "name": "test"
        }
        url = 'http://127.0.0.1:8000/customers/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def create_account(self):
        self.test_customer = Customer.objects.create(name='testCustomer')

        data = {
            "customer": 1,
            "balance": 10
        }
        url = 'http://127.0.0.1:8000/accounts/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def create_transfer(self):
        self.test_customer = Customer.objects.create(name='testCustomer')
        self.account1 = Account.objects.create(customer=1, balance=10)
        self.account2 = Account.objects.create(customer=1, balance=20)

        data = {
            "sender": 1,
            "receiver": 2,
            "balance": 5
        }
        url = 'http://127.0.0.1:8000/transfers/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url3 = reverse('account:transfers-detail', kwargs={'id': 1})
        response3 = self.client.get(url3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

