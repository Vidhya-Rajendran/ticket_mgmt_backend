from django.urls import path
from .views import list_tickets, create_ticket, view_ticket, update_ticket, delete_ticket

urlpatterns = [
    path('tickets/', list_tickets, name='list_tickets'),
    path('ticket/create/', create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/update/', update_ticket, name='update_ticket'),
    path('ticket/<int:ticket_id>/delete/', delete_ticket, name='delete_ticket'),
]