import random
from django.shortcuts import render, redirect
from accounts.models import Client
from .models import Ticket, IssueCategory, SubIssue
from django.http import JsonResponse

# Create your views here.

def generate_ticket_number():
    return "TKT" + str(random.randint(10000, 99999))


def create_ticket(request):

    if not request.session.get('client_id'):
        return redirect('login')

    if request.method == 'POST':
        client = Client.objects.get(id=request.session.get('client_id'))

        issue_id = request.POST.get('issue')
        sub_issue_id = request.POST.get('sub_issue')
        description = request.POST.get('description')

        ticket_number = generate_ticket_number()

        Ticket.objects.create(
            ticket_number=ticket_number,
            client=client,
            issue_id=issue_id,
            sub_issue_id=sub_issue_id,
            description=description
        )

        return redirect('ticket_success', ticket_number=ticket_number)

    issues = IssueCategory.objects.all()
    issues = IssueCategory.objects.all()

    return render(request, 'tickets/create_ticket.html', {
        'issues': issues
    })
    

    return render(request, 'tickets/create_ticket.html', {
        'issues': issues,
        'sub_issues': sub_issues
    })


def ticket_success(request, ticket_number):
    return render(request, 'tickets/success.html', {'ticket_number': ticket_number})


def get_sub_issues(request):
    issue_id = request.GET.get('issue_id')

    sub_issues = SubIssue.objects.filter(issue_id=issue_id)

    data = [
        {'id': sub.id, 'name': sub.name}
        for sub in sub_issues
    ]

    return JsonResponse(data, safe=False)

def track_ticket(request):

    ticket = None
    error = None

    if request.method == 'POST':
        ticket_number = request.POST.get('ticket_number')

        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            error = "Ticket not found"

    return render(request, 'tickets/track_ticket.html', {
        'ticket': ticket,
        'error': error
    })
    
# Create your views here.
