from django.db import models
from account.models import User
from django.utils.timesince import timesince
import uuid
# Create your models here.
class Conversation(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    #auto now is updated every-time this model is saved
    modified_at = models.DateTimeField(auto_now=True)
    
    def created_at_formatted(self):
       return timesince(self.created_at)
   
    def modified_at_formatted(self):
       return timesince(self.modified_at)
    
    class Meta:
        ordering = ('created_at',)

class ConversationMessage(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    
    body = models.TextField(blank=True, null=True)
    sent_to = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    created_by = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    
    def created_at_formatted(self):
       return timesince(self.created_at)