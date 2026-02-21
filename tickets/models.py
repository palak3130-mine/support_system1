from django.db import models
from accounts.models import Client
from dashboard.models import Staff
from django.utils import timezone


# Create your models here.

#ISSUE CATEGORY MODEL
class IssueCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#SUB ISSUE MODEL
class SubIssue(models.Model):
    issue = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#TICKET MODEL
class Ticket(models.Model):

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]


    ticket_number = models.CharField(max_length=20, unique=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    issue = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    sub_issue = models.ForeignKey(SubIssue, on_delete=models.CASCADE)

    description = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    assigned_to = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ticket_number

    def save(self, *args, **kwargs):

        is_new = self._state.adding

        # Assign time
        if self.assigned_to and not self.assigned_at:
            self.assigned_at = timezone.now()
            self.status = 'ASSIGNED'

        # Resolve time
        if self.status == 'RESOLVED' and not self.resolved_at:
            self.resolved_at = timezone.now()

        # Close time
        if self.status == 'CLOSED' and not self.closed_at:
            self.closed_at = timezone.now()

        super().save(*args, **kwargs)

    # ---- ACTIVITY LOGGING ----


        if is_new:
            TicketActivity.objects.create(
                ticket=self,
                action="Ticket created"
            )

        # Assigned
        if self.assigned_to and self.status == 'ASSIGNED':
            TicketActivity.objects.create(
                ticket=self,
                action=f"Assigned to {self.assigned_to.name}"
            )

        # Working / Reopen logic
        if self.status == 'IN_PROGRESS':

            already_worked = TicketActivity.objects.filter(
                ticket=self,
                action="Working on the issue"
            ).exists()

            if already_worked:
                TicketActivity.objects.create(
                    ticket=self,
                    action="Reopened"
                )
            else:
                TicketActivity.objects.create(
                    ticket=self,
                    action="Working on the issue"
                )

        # Resolved
        if self.status == 'RESOLVED':
            TicketActivity.objects.create(
                ticket=self,
                action="Ticket resolved"
            )

        # Closed
        if self.status == 'CLOSED':
            TicketActivity.objects.create(
                ticket=self,
                action="Ticket closed"
            )


class TicketActivity(models.Model):

    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket.ticket_number} - {self.action}"