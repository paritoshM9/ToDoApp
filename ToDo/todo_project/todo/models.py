from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    status = models.TextField(default="")
    #time = models.TimeField((u"Conversation Time"), blank=True)
