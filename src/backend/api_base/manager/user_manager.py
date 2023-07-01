from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(
#         self, email, password=None, is_staff=False, is_superuser=False, is_active=True
#     ):
#         if not email:
#             raise ValueError("User must have an email address")
#         if not password:
#             raise ValueError("User must have an password")
#         user_obj = self.model(email=self.normalize_email(email))
#         user_obj.set_password(password)
#         user_obj.is_staff = is_staff
#         user_obj.is_superuser = is_superuser
#         user_obj.is_active = is_active
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_staff(self, email, password=None):
#         user_obj = self.create_user(email, password=password, is_staff=True)
#         return user_obj

#     def create_superuser(self, email, password=None):
#         user_obj = self.create_user(
#             email, password=password, is_staff=True, is_superuser=True
#         )
#         return user_obj

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('role','ADMIN')
        return self._create_user(email, password, first_name, last_name, **extra_fields)