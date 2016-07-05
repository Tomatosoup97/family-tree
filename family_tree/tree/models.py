from django.db import models
from django.contrib.auth.models import AbstractUser

class FamilyMember(AbstractUser):
    parents = models.ManyToManyField(
        'self', blank=True, related_name='parents')
    children = models.ManyToManyField(
        'self', blank=True, related_name='childs')

    def __str__(self):
        return self.first_name + self.last_name