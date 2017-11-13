from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manages the custom user model. In our case it is UserProfile class"""

    def _create_user(self,email,password,** extra_fields):
        """ creates a new user model"""

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,email,password, **extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)


    def create_superuser(self, email,password, **extra_fields):
        """ Creates and saves a new superuser"""
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a User in our system"""

    first_name = models.CharField(max_length=255, null= True)
    last_name = models.CharField(max_length=255, null = True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/profile-blank.jpg', null = True)
    email = models.EmailField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """ Used to get a user full name"""
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        """ Used to get a users short name"""
        return self.last_name

    def __str__(self):
        """ Converts the object into string"""
        return self.first_name+" "+self.last_name + " - " + self.email

