from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    Plalyst_title = models.CharField(max_length=500,default='Default')

    def __str__(self):
        return self.Plalyst_title
