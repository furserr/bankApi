from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404

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
        newAccount = Account(customer=self, amount=0)
        newAccount.save()



class Account(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', related_name='customerAccount',
                                 on_delete=models.CASCADE)
    amount = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Account'
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.customer, self.amount)

class Transfer(models.Model):
    sender = models.ForeignKey(Account, related_name='senderAccount', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='receiverAccount', on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        verbose_name_plural = 'Transfer'
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.sender, self.receiver)

    def save(self, *args, **kwargs):
        senderAccount = get_object_or_404(Account, id=self.sender.id)
        receiverAccount = get_object_or_404(Account, id=self.receiver.id)
        if senderAccount != receiverAccount:
            senderAccount.amount = senderAccount.amount - self.amount
            receiverAccount.amount = receiverAccount.amount + self.amount
            senderAccount.save()
            receiverAccount.save()
            super(Transfer, self).save(*args, **kwargs)
        else:
            return Http404('<h1>Same accounts</h1>')