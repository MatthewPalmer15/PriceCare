from django.contrib import admin
from .models import Subscription, Provider, Frequency

# Register the models in the admin site
admin.site.register(Subscription)
admin.site.register(Provider)
admin.site.register(Frequency)
