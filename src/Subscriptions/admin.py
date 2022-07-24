from django.contrib import admin
from .models import Subscription, Provider, Frequency

admin.site.register(Subscription)
admin.site.register(Provider)
admin.site.register(Frequency)