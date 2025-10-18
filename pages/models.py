from django.db import models

class Profile(models.Model):
    headline = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    github = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.email or 'Profile'

# Create your models here.
