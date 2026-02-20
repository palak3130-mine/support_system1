from django.db import models

class Client(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    org_name = models.CharField(max_length=200)
    COMPANY_TYPE_CHOICES = [
    ('AMC', 'AMC'),
    ('NON_AMC', 'NON AMC'),
    ('HAND_HOLDING', 'Hand Holding'),
    ('OTHER', 'Other'),
]

    company_type = models.CharField(max_length=20, choices=COMPANY_TYPE_CHOICES)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name