# dashboard/models.py

from django.db import models


# ===============================
# STAFF MODEL
# ===============================
class Staff(models.Model):

    # Basic info
    name = models.CharField(max_length=100)

    # Speciality linked to Issue Category
    speciality = models.ForeignKey(
        'tickets.IssueCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Contact info
    email = models.EmailField()

    # Login credentials (custom auth)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name