from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator
)
from .managers import UserManager
from .constants import GENDER_CHOISE

# Create your models here.

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    
    def __str__(self):
        return self.email
    
    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0

class BankAccountType(models.Model):
    name = models.CharField(max_length=128)
    maximum_withdeawl_account = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    
    def __str__(self):
        return self.name
class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User,
        related_name='account',
        on_delete=models.CASCADE
    )
    account_type = models.ForeignKey(
        BankAccountType,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    account_no = models.PositiveBigIntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISE)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    initial_deposit_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(
        User,
        related_name='address',
        on_delete=models.CASCADE
    )
    street_address = models.CharField(max_length=52)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.email
    
    
