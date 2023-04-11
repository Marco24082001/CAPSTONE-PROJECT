import uuid
# from api_base.manager import UserManager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile, password, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
    

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # google_login = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True, null=True)
    # first_name = None
    # last_name = None
    # username = None
    # EMAIL_FIELD = 'email'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = UserManager()

    class Meta:
        db_table = "users"
        # ordering = ('date_joined',)

    def __str__(self):
        return str(self.email)
