from django.urls import path
from .views import portal_home, staff_login, staff_dashboard, staff_logout, admin_panel

urlpatterns = [
    path('', portal_home, name='portal_home'),
    path('login/', staff_login, name='staff_login'),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
    path('logout/', staff_logout, name='staff_logout'),
    path('admin-panel/', admin_panel, name='admin_panel'),
]