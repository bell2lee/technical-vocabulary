from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True, verbose_name="이메일")
    name = models.CharField(max_length=15, null=False, verbose_name="이름")
    nickname = models.CharField(max_length=20, null=False, unique=True, verbose_name="닉네임")
    is_active = models.BooleanField(default=True, verbose_name="활성화")
    is_admin = models.BooleanField(default=False, verbose_name="관리자 여부")
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']