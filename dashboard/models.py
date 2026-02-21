from django.contrib.auth.models import User
from django.db import models

class Staff(models.Model):

    name = models.CharField(max_length=100)
    speciality = models.ForeignKey('tickets.IssueCategory', on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name