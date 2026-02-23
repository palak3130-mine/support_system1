# tickets/admin.py

from django.contrib import admin
from .models import Ticket, IssueCategory, SubIssue, TicketActivity


admin.site.register(Ticket)
admin.site.register(IssueCategory)
admin.site.register(SubIssue)
admin.site.register(TicketActivity)