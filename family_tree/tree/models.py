from django.db import models
from django.contrib.auth.models import AbstractUser

class FamilyMember(AbstractUser):
    parents = models.ManyToManyField('self', related_name='parents')
    children = models.ManyToManyField('self', related_name='children')

    born = models.DateTimeField('born date', db_index=True)
    died = models.DateTimeField(
        'date of death', db_index=True, null=True, blank=True)

    def __str__(self):
        return self.first_name + self.last_name

    def years(self):
        return self.died.year - self.born.year