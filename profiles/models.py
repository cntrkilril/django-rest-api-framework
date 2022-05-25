from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True, default='...')
    location = models.CharField(max_length=100, null=True, blank=True)

    def get_username(self):
        return self.username
