from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("role"):
            from .user import Role
            extra_fields["role"] = Role.objects.get_default_user_role()
        return self._create_user(email, password, **extra_fields)





class RoleManager(models.Manager):

    def get_default_user_role(self):
        role, created = self.get_or_create(
            name="user",
            defaults={"is_active": True}
        )
        return role
