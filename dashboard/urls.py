from django.urls import path
from .views import portal_home, staff_login, staff_dashboard, staff_logout, admin_panel, ticket_detail
from .views import update_ticket_status
from . import views

urlpatterns = [
    path('', portal_home, name='portal_home'),
    path('login/', staff_login, name='staff_login'),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
    path('logout/', staff_logout, name='staff_logout'),
    path('admin-panel/', admin_panel, name='admin_panel'),
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/status/<str:status>/', update_ticket_status, name='update_ticket_status'),
    path('staff-login/', staff_login, name='staff_login'),
    path('ticket/<int:ticket_id>/', views.staff_ticket_detail, name='staff_ticket_detail'),
]