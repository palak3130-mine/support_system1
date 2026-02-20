from django.contrib import admin
from .models import Ticket, IssueCategory, SubIssue
from dashboard.models import Staff


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    # 👇 THIS LINE SHOWS TIMES IN ADMIN
    readonly_fields = ('created_at', 'assigned_at')

    # 👇 FILTER STAFF BASED ON ISSUE
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "assigned_to":
            ticket_id = request.resolver_match.kwargs.get('object_id')

            if ticket_id:
                try:
                    ticket = Ticket.objects.get(id=ticket_id)
                    kwargs["queryset"] = Staff.objects.filter(speciality=ticket.issue)
                except Ticket.DoesNotExist:
                    pass

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(IssueCategory)
admin.site.register(SubIssue)