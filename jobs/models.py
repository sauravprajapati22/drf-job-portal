from django.db import models
from django.conf import settings

# Create your models here.
class job(models.Model):
    title        = models.CharField(max_length=50)
    descriptions = models.TextField()
    company_name = models.CharField(max_length=100)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="jobs")
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

