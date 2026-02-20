from django.urls import path
from .views import login_view, logout_view, client_dashboard

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', client_dashboard, name='client_dashboard'),
    path('logout/', logout_view, name='logout'),
]