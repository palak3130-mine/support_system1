# tickets/models.py

from django.db import models
from accounts.models import Client
from dashboard.models import Staff


# ===============================
# ISSUE CATEGORY MODEL
# ===============================
class IssueCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ===============================
# SUB ISSUE MODEL
# ===============================
class SubIssue(models.Model):
    issue = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ===============================
# MAIN TICKET MODEL
# ===============================
class Ticket(models.Model):

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('WORKING', 'Working'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    ticket_number = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    issue = models.ForeignKey(IssueCategory, on_delete=models.SET_NULL, null=True)
    sub_issue = models.ForeignKey(SubIssue, on_delete=models.SET_NULL, null=True)

    description = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    assigned_to = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ticket_number


# ===============================
# ACTIVITY TIMELINE MODEL
# ===============================
class TicketActivity(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="activities")
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket.ticket_number} - {self.message}"