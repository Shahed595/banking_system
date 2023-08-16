from django.db import models
from .constants import TRANSACTION_TYPE_CHOICES
from accounts.models import UserBankAccount

# Create your models here.

class Transactions(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name='transactions',on_delete=models.CASCADE, null=True,blank=True)
    
    ammount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    
    balance_after_transactions = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE_CHOICES, null=True)
    
    timestamp = models.DateField(auto_now_add=True)
    loan_approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']
