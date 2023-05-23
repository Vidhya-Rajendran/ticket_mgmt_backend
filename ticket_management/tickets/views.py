from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ticket
from ticket_management.employee.models import Employee, EmployeeDutyRoster
from django.utils import timezone
from datetime import datetime

# Create your views here.
from django.db.models import Q

@api_view(['GET'])
def list_tickets(request):
    search_query = request.GET.get('search')
    tickets = Ticket.objects.all().order_by('-id')
    if search_query:
        tickets = tickets.filter(
            Q(number__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    # Return the filtered tickets
    data = [{
        'id': ticket.id,
        'number': ticket.number, 
        'created_at': ticket.created_at.strftime("%d %b, %Y"), 
        'description': ticket.description, 
        'resolution_end_date': ticket.resolution_end_date.strftime("%d %b, %Y"),
        'status': ticket.status,
        'assigned_to': ticket.assigned_to.name if ticket.assigned_to else 'Unassigned'
        } for ticket in tickets]
    return Response(data)


@api_view(['POST'])
def create_ticket(request):
    description = request.data.get('description')
    resolution_end_date = request.data.get('resolution_end_date')

    # Get the next available employee based on the employee duty roster schedule
    next_employee_roster = EmployeeDutyRoster.objects.filter(date__lte=timezone.now(), is_employee_available=True).order_by('id').first()
    
    # Get the next available employee based on round robin
    employee_index = Ticket.objects.count() % Employee.objects.count()
    print(employee_index, Ticket.objects.count(), Employee.objects.count())
    employee = Employee.objects.filter(is_available=True)[employee_index]
    print(employee, employee_index)

    if next_employee_roster:
        # Create the ticket object
        ticket = Ticket.objects.create(
            description=description,
            resolution_end_date=resolution_end_date,
            status='In Progress',
            assigned_to_id=next_employee_roster.employee_id
        )

        next_employee_roster.is_employee_available = False
        next_employee_roster.ticket.add(ticket)
        next_employee_roster.save()

        return Response({'message': 'Ticket created successfully', 'ticket_id': ticket.id})
    elif employee:
        # Create the ticket object
        ticket = Ticket.objects.create(
            description=description,
            resolution_end_date=resolution_end_date,
            status='In Progress',
            assigned_to_id=employee.id
        )

        return Response({'message': 'Ticket created successfully', 'ticket_id': ticket.id})
    else:
        return Response({'message': 'No available employees found'})


@api_view(['GET'])
def view_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({'message': 'Ticket not found'}, status=404)

    # Return the ticket details
    data = {
        'id': ticket.id,
        'number': ticket.number, 
        'created_at': ticket.created_at.strftime("%d %b, %Y"), 
        'description': ticket.description, 
        'resolution_end_date_formatted': ticket.resolution_end_date.strftime("%d %b, %Y"),
        'resolution_end_date': ticket.resolution_end_date,
        'status': ticket.status,
        'assigned_to': ticket.assigned_to.name if ticket.assigned_to else 'Unassigned'
    }
    return Response(data)


@api_view(['PUT'])
def update_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({'message': 'Ticket not found'}, status=404)

    # Update the ticket
    ticket.status = request.data.get('status')
    ticket.description = request.data.get('description')
    ticket.resolution_end_date = request.data.get('resolution_end_date')
    ticket.save()

    return Response({'message': 'Ticket updated successfully'})


@api_view(['DELETE'])
def delete_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({'message': 'Ticket not found'}, status=404)

    # Delete the ticket
    EmployeeDutyRoster.objects.filter(ticket=ticket).update(is_employee_available=True)
    ticket.delete()

    return Response({'message': 'Ticket deleted successfully'})


