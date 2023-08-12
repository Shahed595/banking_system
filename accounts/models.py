from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator
)
from .managers import UserManager

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
    
