from django.shortcuts import render, redirect
from .models import Staff
from tickets.models import Ticket
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404


def staff_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            staff = Staff.objects.get(username=username, password=password)

            request.session['staff_id'] = staff.id

            return redirect('staff_dashboard')

        except Staff.DoesNotExist:
            return render(request, 'staff/login.html', {'error': 'Invalid credentials'})

    return render(request, 'staff/login.html')


# Portal landing page
def portal_home(request):
    return render(request, 'dashboard/portal_home.html')


# Staff login

def staff_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            staff = Staff.objects.get(username=username, password=password)

            request.session['staff_id'] = staff.id

            return redirect('staff_dashboard')

        except Staff.DoesNotExist:
            return render(request, 'staff/login.html', {'error': 'Invalid username or password'})

    return render(request, 'staff/login.html')


# Staff dashboard
def staff_dashboard(request):

    staff_id = request.session.get('staff_id')

    if not staff_id:
        return redirect('staff_login')

    staff = Staff.objects.get(id=staff_id)

    tickets = Ticket.objects.filter(assigned_to=staff)

    return render(request, 'dashboard/staff_dashboard.html', {
        'tickets': tickets,
        'staff': staff
    })


# Logout
def staff_logout(request):
    request.session.flush()
    return redirect('staff_login')


def admin_panel(request):

    total = Ticket.objects.count()
    open_tickets = Ticket.objects.filter(status='OPEN').count()
    assigned = Ticket.objects.filter(status='ASSIGNED').count()
    resolved = Ticket.objects.filter(status='RESOLVED').count()
    closed = Ticket.objects.filter(status='CLOSED').count()

    recent = Ticket.objects.order_by('-created_at')[:5]

    return render(request, 'dashboard/admin_panel.html', {
        'total': total,
        'open': open_tickets,
        'assigned': assigned,
        'resolved': resolved,
        'closed': closed,
        'recent': recent
    })


def ticket_detail(request, ticket_id):

    ticket = Ticket.objects.get(id=ticket_id)
    activities = ticket.activities.all().order_by('-timestamp')

    return render(request, 'dashboard/ticket_detail.html', {
        'ticket': ticket,
        'activities': activities
    })


def update_ticket_status(request, ticket_id, status):

    ticket = Ticket.objects.get(id=ticket_id)

    # If already closed → block updates
    if ticket.status == 'CLOSED':
        return redirect('ticket_detail', ticket_id=ticket.id)

    ticket.status = status
    ticket.save()

    return redirect('ticket_detail', ticket_id=ticket.id)


def staff_ticket_detail(request, ticket_id):

    staff_id = request.session.get('staff_id')

    if not staff_id:
        return redirect('staff_login')

    staff = Staff.objects.get(id=staff_id)

    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Security check
    if ticket.assigned_to != staff:
        return redirect('staff_dashboard')

    return render(request, 'staff/ticket_detail.html', {'ticket': ticket})