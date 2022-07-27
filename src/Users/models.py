from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    """ Create either a normal user or a superuser """
    # Creating a normal user
    def create_user(self, email, password, **extra_fields):
        """ Create and save a new user """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    # Creating a superuser
    def create_superuser(self, email, password, **extra_fields):
        """ Create and save a new superuser """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ The user account model that is used by the authentication system """
    id          = models.AutoField(
                    primary_key=True
                )
    profilepic  = models.ImageField(
                    upload_to='Static/images/profilepics/',
                    default='Static/images/profilepics/default.png',
                    blank=True,
                    null=True
                )
    username    = models.CharField(
                    max_length=32,
                    unique=True
                )
    first_name  = models.CharField(
                    max_length=64
                )
    last_name   = models.CharField(
                    max_length=64
                )
    email       = models.EmailField(
                    max_length=128,
                    unique=True
                )
    password    = models.CharField(
                    max_length=512
                )
    is_staff    = models.BooleanField(
                    _('staff'),
                    default=False
                )
    is_active   = models.BooleanField(
                    _('active'),
                    default=True
                )

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


class SupportTicket(models.Model):
    """ Support ticket that a user can submit """
    id          = models.AutoField(
                    primary_key=True
                )
    user        = models.ForeignKey(
                    to=User,
                    on_delete=models.CASCADE
                )
    subject     = models.CharField(
                    max_length=64,
                    default="No Subject"
                )
    message     = models.TextField(
                    max_length=512
                )
    file        = models.FileField(
                    upload_to='Static/files/support/',
                    blank=True,
                    null=True
                )
    created_at  = models.DateTimeField(
                    auto_now_add=True
                )
    is_closed   = models.BooleanField(
                    default=False
                )

    def __str__(self):
        return f"Ticket No. {self.id} - {self.subject}" 

    @property
    def responses(self):
        """ Get the response to the support ticket """
        return SupportTicketResponse.objects.filter(ticket=self)

    @property
    def filename(self):
        """ Get the filename of the file """
        if self.file:
            return self.file.name.split('/')[-1]
        return None

    @property
    def filesize(self):
        """ Get the file size in KB """
        if self.file:
            return round(self.file.size / 1024, 2)
        return 0

class SupportTicketResponse(models.Model):
    """ Support ticket response that a user can submit """
    id          = models.AutoField(
                    primary_key=True
                )
    user        = models.ForeignKey(
                    to=User,
                    on_delete=models.CASCADE
                )
    ticket      = models.ForeignKey(
                    to=SupportTicket,
                    on_delete=models.CASCADE
                )
    message     = models.TextField(
                    max_length=512
                )
    file        = models.FileField(
                    upload_to='Static/files/support/',
                    blank=True,
                    null=True
                )
    created_at  = models.DateTimeField(
                    auto_now_add=True
                )

    def __str__(self):
        return f"Ticket No. {self.ticket.id} - {self.ticket.subject} (Response No. {self.id})"

    @property
    def filename(self):
        """ Get the filename of the file """
        if self.file:
            return self.file.name.split('/')[-1]
        return None

    @property
    def filesize(self):
        """ Get the file size in KB """
        if self.file:
            return round(self.file.size / 1024, 2)
        return 0