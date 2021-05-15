from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.mide(email=email, name=name)

        user.set_password(password)
        user.save()

        return.user


class UserAccount(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=55, unique=True)
    is_active = models.BoleanField(default=True) 
    is_active = models.BoleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name


     def get_short_name(self):
        return self.name

     def __str__(self):
        return self.email
