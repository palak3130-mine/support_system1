from django.urls import path
from .views import create_ticket, ticket_success, get_sub_issues, track_ticket

urlpatterns = [
    path('create/', create_ticket, name='create_ticket'),
    path('success/<str:ticket_number>/', ticket_success, name='ticket_success'),
    path('get-sub-issues/', get_sub_issues, name='get_sub_issues'),
    path('track/', track_ticket, name='track_ticket'),
]