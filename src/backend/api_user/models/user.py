import uuid
# from api_base.manager import UserManager

from django.db import models
from django.contrib.auth.models import AbstractUser
from api_user.constants import Roles
from api_base.models import BaseModel
from api_base.manager import CustomUserManager




class User(BaseModel, AbstractUser):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField(null=True)
    address = models.TextField(null=True)
    avatar = models.CharField(max_length=250, default='https://res.cloudinary.com/h-b-ch-khoa/image/upload/v1640271647/riunwzwz8xgft7fwohmc.jpg')
    role = models.CharField(choices=Roles.choices(), default=Roles.USER.value, max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    username = None

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    fields_save_in_fabric = ['id', 'password', 'email', 'role']


    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = "users"
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-created_at',)
        # ordering = ('date_joined',)

    def __str__(self):
        return str(self.email)
    
    # Abstractbaseuser has password, last_login, is_active by default