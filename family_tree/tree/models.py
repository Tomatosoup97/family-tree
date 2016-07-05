from django.db import models
from django.contrib.auth.models import AbstractUser

class FamilyMember(AbstractUser):

    father = models.ForeignKey('self', related_name='father')
    mother = models.ForeignKey('self', related_name='mother')
    sons = models.ManyToManyField(
        'self', blank=True, related_name='sons')
    daughters = models.ManyToManyField(
        'self', blank=True, related_name='daughter')

    born = models.DateTimeField('born date', db_index=True)
    died = models.DateTimeField(
        'date of death', db_index=True, null=True, blank=True)

    def __str__(self):
        return self.first_name + self.last_name