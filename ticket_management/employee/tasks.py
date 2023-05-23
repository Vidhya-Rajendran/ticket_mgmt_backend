from celery import shared_task
from .models import Employee, EmployeeDutyRoster
from ..tickets.models import Ticket
from datetime import datetime, timedelta

@shared_task
def generate_employee_roster():
    print('Generating Employee Roster')
    # Get all employees
    employees = Employee.objects.all(is_available=True)

    # Calculate the duration for each employee
    duration = timedelta(hours=8)

    # Get the current date and time
    today = datetime.now()

    # Generate duty roster based on business rules
    for i, employee in enumerate(employees):
        # Calculate the start time and end time for each employee
        start_time = today + timedelta(days=i)
        end_time = start_time + duration

        # Create EmployeeDutyRoster entry
        EmployeeDutyRoster.objects.create(
            employee=employee,
            date=today.date(),
            start_time=start_time,
            end_time=end_time,
            is_employee_available=True
        )
    print('Employee Roster generated successfully')
