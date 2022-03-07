from unicodedata import category
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Scholarship(models.Model):
    title = models.CharField(max_length = 200)
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    application_open = models.DateTimeField(blank=True)
    application_deadline = models.DateTimeField(blank=True)
    type = models.ManyToManyField(Type)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title