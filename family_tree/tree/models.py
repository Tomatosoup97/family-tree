from datetime import date

from django.db import models

class FamilyMember(models.Model):
    first_name = models.CharField('first name', max_length=200)
    last_name = models.CharField('last name', max_length=200)
    family_name = models.CharField('family name', max_length=200, blank=True)

    parents = models.ManyToManyField(
            'self', related_name='children', blank=True, symmetrical=False)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    image = models.ImageField('image', blank=True)
    description = models.TextField('description')
    born = models.DateField('born date', db_index=True)
    died = models.DateField(
            'date of death', db_index=True, null=True, blank=True,
            help_text='leave empty if member is still alive')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def years(self):
        return self.died.year - self.born.year

    def passed_away(self):
        if died:
            return date.today().year - self.died.year
        else:
            return "This family member is still living"