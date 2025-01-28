from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-end_time']

    def __str__(self):
        return f"{self.description} ({self.duration})"

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.end_time - self.start_time
        super().save(*args, **kwargs)