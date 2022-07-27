from django.contrib import admin
from .models import User, SupportTicket, SupportTicketResponse

# Register the models in the admin site
admin.site.register(User)
admin.site.register(SupportTicket)
admin.site.register(SupportTicketResponse)