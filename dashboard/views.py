from django.shortcuts import render, redirect
from .models import Staff
from tickets.models import Ticket


# Portal landing page
def portal_home(request):
    return render(request, 'dashboard/portal_home.html')


# Staff login
def staff_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            staff = Staff.objects.get(email=email)
            request.session['staff_id'] = staff.id
            return redirect('staff_dashboard')

        except Staff.DoesNotExist:
            return render(request, 'dashboard/staff_login.html', {'error': 'Invalid email'})

    return render(request, 'dashboard/staff_login.html')


# Staff dashboard
def staff_dashboard(request):

    if not request.session.get('staff_id'):
        return redirect('staff_login')

    staff = Staff.objects.get(id=request.session.get('staff_id'))
    tickets = Ticket.objects.filter(assigned_to=staff)

    return render(request, 'dashboard/staff_dashboard.html', {
        'staff': staff,
        'tickets': tickets
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