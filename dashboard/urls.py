from django.urls import path
from . import views

urlpatterns = [

    # Portal
    path('', views.portal_home, name='portal_home'),

    # Staff auth
    path('staff-login/', views.staff_login, name='staff_login'),
    path('dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('logout/', views.staff_logout, name='staff_logout'),

    # Staff ticket
    path("staff/ticket/<int:ticket_id>/", views.staff_ticket_detail, name="staff_ticket_detail"),
    path('ticket/<int:ticket_id>/status/<str:status>/', views.staff_update_status, name='staff_update_status'),
    path('ticket/<int:ticket_id>/comment/', views.add_comment, name='add_comment'),

    # Admin
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path("admin/ticket/<int:ticket_id>/", views.admin_ticket_detail, name="admin_ticket_detail"),

    # Client
    path("client/ticket/<int:ticket_id>/", views.client_ticket_detail, name="client_ticket_detail"),
    
]