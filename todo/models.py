from django.db import models
from django.utils import timezone
from base.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    due_to = models.DateTimeField(default=timezone.now, null=None, blank=None)
    completed = models.BooleanField(default=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        
    def __str__(self):
        return f"{self.title} => {self.user.email}" 