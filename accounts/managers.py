from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True#migrations ta true kore dewa hoise(command er jonno)
    
    def create_user(self, email, password, **extra_fields):
        #Create and save a user with the given email, and password.
        if not email:
            raise ValueError('Email Must be set')
        email = self.normalize_email(email)#it will count all the same name email either it's capital or small letters
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password,extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email,password,**extra_fields)
        
            
            
    
    
    