# DJANGO import
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django import forms
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have an email address.")
        if not password:
            raise ValueError("User must have a password.")
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):

        user = self.create_user (
            email,
            password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "@{}".format(self.email)

    
