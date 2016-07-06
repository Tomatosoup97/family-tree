from datetime import date

from django.db import models

class FamilyMember(models.Model):
    first_name = models.CharField('first name', max_length=200)
    last_name = models.CharField('last name', max_length=200)
    family_name = models.CharField('family name', max_length=200, blank=True)
    parents = models.ManyToManyField('self', related_name='parents')
    children = models.ManyToManyField('self', related_name='children')

    image = models.ImageField('image')
    description = models.TextField('description')
    born = models.DateTimeField('born date', db_index=True)
    died = models.DateTimeField(
        'date of death', db_index=True, null=True, blank=True,
        help_text='leave empty if member is still alive')

    def __str__(self):
        return self.first_name + self.last_name

    def years(self):
        return self.died.year - self.born.year

    def passed_away(self):
        if died:
            return date.today().year - self.died.year
        else:
            return "This family member is still living"