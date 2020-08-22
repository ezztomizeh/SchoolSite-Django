from django.db import models
from datetime import datetime
# Create your models here.
class Messages(models.Model):
    Msg_title = models.CharField(max_length=100,default='Untitled')
    Msg_content = models.TextField(null=False)
    Msg_sender = models.CharField(max_length=100,null=False)
    Msg_reciver = models.CharField(max_length=100,null=False)
    Msg_Date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.Msg_title}'