from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Customer'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        newAccount = Account(customer=self, balance=0)
        newAccount.save()



class Account(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', related_name='customerAccount',
                                 on_delete=models.CASCADE)
    balance = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Account'
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.customer, self.balance)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValidationError({'Error':"Balance can not be negative."}, code=400)
        else:
            super(Account, self).save(*args, **kwargs)

class Transfer(models.Model):
    sender = models.ForeignKey(Account, related_name='senderAccount', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='receiverAccount', on_delete=models.CASCADE)
    balance = models.FloatField()

    class Meta:
        verbose_name_plural = 'Transfer'
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.sender, self.receiver)

    def save(self, *args, **kwargs):
        senderAccount = get_object_or_404(Account, id=self.sender.id)
        receiverAccount = get_object_or_404(Account, id=self.receiver.id)
        if senderAccount != receiverAccount:
            senderAccount.balance = senderAccount.balance - self.balance
            receiverAccount.balance = receiverAccount.balance + self.balance
            senderAccount.save()
            receiverAccount.save()
            super(Transfer, self).save(*args, **kwargs)
        else:
            raise ValidationError({'Error':"Sender account and receiver account can not be same accounts."}, code=400)