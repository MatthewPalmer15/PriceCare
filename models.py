from django.db import models
from Users.models import User
from ckeditor.fields import RichTextField

class SupportTicket(models.Model):
    """ Support ticket that a user can submit """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=128)
    message = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id 

class SupportTicketResponse(models.Model):
    """ Support ticket response that a user can submit """
    id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(to=SupportTicket, on_delete=models.CASCADE)
    message = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)