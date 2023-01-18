from django.db import models

class Task(models.Model):
    body = models.TextField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    check = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-time_created"]
    def __str__(self):
        return self.body
