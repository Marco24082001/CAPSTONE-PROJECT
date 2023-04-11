import uuid
# from api_base.manager import UserManager

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from api_base.models import BaseModel
from api_base.manager import CustomUserManager




class User(BaseModel, AbstractUser):
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
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    address = models.CharField( max_length=250)

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']