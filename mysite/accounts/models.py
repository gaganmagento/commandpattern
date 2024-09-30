from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
# Create your models here.

    def __str__(self):
        return self.username