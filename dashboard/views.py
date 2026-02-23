from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from tickets.models import Ticket, TicketActivity


# ================================
# 🌐 PORTAL HOME
# ================================
def portal_home(request):
    return render(request, "dashboard/portal_home.html")


# ================================
# 👨‍💻 STAFF LOGIN
# ================================
def staff_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            staff = Staff.objects.get(username=username, password=password)
            request.session["staff_id"] = staff.id
            return redirect("staff_dashboard")
        except Staff.DoesNotExist:
            return render(request, "staff/login.html", {"error": "Invalid credentials"})

    return render(request, "staff/login.html")


# ================================
# 🚪 STAFF LOGOUT
# ================================
def staff_logout(request):
    request.session.flush()
    return redirect("staff_login")


# ================================
# 📊 STAFF DASHBOARD
# ================================
def staff_dashboard(request):
    staff_id = request.session.get("staff_id")

    if not staff_id:
        return redirect("staff_login")

    staff = Staff.objects.get(id=staff_id)

    tickets = Ticket.objects.filter(assigned_to=staff).order_by("-created_at")

    return render(request, "dashboard/staff_dashboard.html", {
        "staff": staff,
        "tickets": tickets
    })


# ================================
# 🎫 STAFF TICKET DETAIL
# ================================
def staff_ticket_detail(request, ticket_id):
    staff_id = request.session.get("staff_id")

    if not staff_id:
        return redirect("staff_login")

    ticket = get_object_or_404(Ticket, id=ticket_id)

    activities = TicketActivity.objects.filter(ticket=ticket).order_by("-timestamp")

    return render(request, "staff/ticket_detail.html", {
        "ticket": ticket,
        "activities": activities,
    })


# ================================
# 🔄 STAFF UPDATE STATUS
# ================================
def staff_update_status(request, ticket_id, status):
    staff_id = request.session.get("staff_id")

    if not staff_id:
        return redirect("staff_login")

    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Only allow WORKING + RESOLVED
    if status == "WORKING":
        ticket.status = "WORKING"
        TicketActivity.objects.create(ticket=ticket, message="Working on the issue")

    elif status == "RESOLVED":
        ticket.status = "RESOLVED"
        ticket.resolved_at = ticket.resolved_at or ticket.created_at
        TicketActivity.objects.create(ticket=ticket, message="Ticket resolved")

    ticket.save()

    return redirect("staff_ticket_detail", ticket_id=ticket.id)


# ================================
# 💬 ADD COMMENT
# ================================
def add_comment(request, ticket_id):
    staff_id = request.session.get("staff_id")

    if not staff_id:
        return redirect("staff_login")

    if request.method == "POST":
        message = request.POST.get("message")

        ticket = get_object_or_404(Ticket, id=ticket_id)
        staff = Staff.objects.get(id=staff_id)

        Comment.objects.create(
            ticket=ticket,
            staff=staff,
            message=message
        )

    return redirect("staff_ticket_detail", ticket_id=ticket_id)


# ================================
# 🛠 ADMIN PANEL
# ================================
def admin_panel(request):
    tickets = Ticket.objects.all().order_by("-created_at")

    return render(request, "dashboard/admin_panel.html", {
        "tickets": tickets
    })

# ================================
# 🛠 ADMIN TICKET DETAIL
# ================================
def admin_ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    activities = TicketActivity.objects.filter(ticket=ticket).order_by("-timestamp")

    return render(request, "dashboard/admin_ticket_detail.html", {
        "ticket": ticket,
        "activities": activities
    })
# ================================
# 🛠 CLIENT TICKET DETAIL
# ================================
def client_ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    activities = TicketActivity.objects.filter(ticket=ticket).order_by("-timestamp")

    return render(request, "dashboard/ticket_detail.html", {
        "ticket": ticket,
        "activities": activities
    })