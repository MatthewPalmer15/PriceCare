from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    # Creating a normal user
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    # Creating a superuser
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id           = models.AutoField(primary_key=True)
    profilepic   = models.ImageField(upload_to='Static/images/profilepics/', default='Static/images/profilepics/default.png', blank=True, null=True)
    username     = models.CharField(max_length=32, unique=True)
    first_name   = models.CharField(max_length=64)
    last_name    = models.CharField(max_length=64)
    email        = models.EmailField(max_length=128, unique=True)
    password     = models.CharField(max_length=8192)
    is_staff     = models.BooleanField(_('staff'), default=False)
    is_active    = models.BooleanField(_('active'), default=True)

    # This tells django to use the email as the main sign in field.
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
    ]

    def __str__(self):
        return self.username

    objects = CustomAccountManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
