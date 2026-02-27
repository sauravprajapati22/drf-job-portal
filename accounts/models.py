from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('employee','Employee'),
        ('job_seeker','Job_seeker')
    )

    role = models.CharField(max_length=25,choices=ROLE_CHOICES)

    def __str__(self):
        return self.username