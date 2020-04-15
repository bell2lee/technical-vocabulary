from django.db import models
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class UserManage(BaseUserManager):
    def create_user(self, user_id, password, extra_fields):
        args = extra_fields.copy()
        user = self.model(
            **args
        )
        user.is_active = True
        user.save(using=self._db)
        return user
