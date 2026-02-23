# accounts/models.py

from django.db import models


# ===============================
# CLIENT MODEL
# ===============================
class Client(models.Model):

    # Login credentials
    user_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    # Organization info
    org_name = models.CharField(max_length=200)

    COMPANY_TYPE_CHOICES = [
        ('AMC', 'AMC'),
        ('NON_AMC', 'NON AMC'),
        ('HAND_HOLDING', 'Hand Holding'),
        ('OTHER', 'Other'),
    ]

    company_type = models.CharField(max_length=20, choices=COMPANY_TYPE_CHOICES)

    # Contact info
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Created timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name