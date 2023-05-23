from django.contrib import admin
from .models import Employee, EmployeeDutyRoster

from rangefilter.filters import DateRangeFilter

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name', 'email', 'phone_number', 'is_available')
    search_fields = ('emp_id', 'name', 'email', 'phone_number')
    list_filter = (
        'is_available',
    )
    fields = ('emp_id', 'name', 'email', 'phone_number', 'is_available')
    readonly_fields = ('emp_id',)
    list_per_page = 25




@admin.register(EmployeeDutyRoster)
class EmployeeDutyRosterAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'start_time', 'end_time', 'is_employee_available')
    search_fields = ('employee__name', 'employee__email', 'employee__phone_number',)
    autocomplete_fields = ("employee", "ticket")
    list_filter = (
        'is_employee_available', 
        ('date', DateRangeFilter),
        'ticket',
    )

    list_per_page = 25