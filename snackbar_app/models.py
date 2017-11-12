from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manages the custom user model. In our case it is UserProfile class"""

    def create_user(self, email, name, password, job_title=None, organization_name=None,
                    phone_country_code=None, phone_number=None, created_on=None, picture=None):
        """ creates a new user model"""

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(name=name, job_title=job_title,
                          organization_name=organization_name,
                          phone_country_code=phone_country_code, phone_number=phone_number, picture=picture,
                          email=email, created_on=created_on)

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """ Creates and saves a new superuser"""

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a User in our system"""

    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255, null=True)
    organization_name = models.CharField(max_length=255, null=True)
    phone_country_code = models.IntegerField(default=0, null=True)
    phone_number = models.IntegerField(default=0, null=True)
    picture = models.ImageField(upload_to='images/', default='images/No-img.jpg',
                                max_length=None, null=True)
    email = models.EmailField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get a user full name"""
        return self.name

    def get_short_name(self):
        """ Used to get a users short name"""
        return self.name

    def __str__(self):
        """ Converts the object into string"""
        return self.name + " - " + self.email



# class UserModel(models.Model):
#     email = models.EmailField(max_length=255, unique=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserProfileManager()
#     USERNAME_FIELD = 'email'
#
