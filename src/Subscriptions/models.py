from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from colorfield.fields import ColorField
from Users.models import User

class Provider(models.Model):
    """ Provider that a user can subscribe to """
    id          = models.AutoField(
                    primary_key=True
                )
    name        = models.CharField(
                    max_length=128
                )
    image       = models.ImageField(
                    upload_to='Static/images/providers/',
                    blank=True,
                    null=True
                )
    colour      = ColorField(
                    default='#000000'
                )

    def __str__(self):
        return self.name

class Frequency(models.Model):
    """ Frequency that a user can subscribe to """
    id          = models.AutoField(
                    primary_key=True
                )
    name        = models.CharField(
                    max_length=64
                )
    days        = models.PositiveIntegerField(
                    default=28
                )

    def __str__(self):
        return self.name

class Subscription(models.Model):
    """ Subscription that a user currently defines """
    id          = models.AutoField(
                    primary_key=True
                )
    user        = models.ForeignKey(
                    to=User,
                    on_delete=models.CASCADE
                )
    provider    = models.ForeignKey(
                    to=Provider,
                    on_delete=models.CASCADE
                )
    amount      = models.DecimalField(
                    decimal_places=2,
                    max_digits=10,
                    validators=[
                        MinValueValidator(Decimal('0.01'))
                    ]
                )
    frequency   = models.ForeignKey(
                    to=Frequency,
                    on_delete=models.CASCADE,
                    default=1
                )

    def __str__(self):
        return f"{self.user.username}'s subscription to {self.provider.name}"
