from django.contrib import admin
from .models import Ticket
from rangefilter.filters import DateRangeFilter


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'assigned_to', 'created_at', 'resolution_end_date')
    readonly_fields = ('number','created_at')
    search_fields = ('number', 'status',)
    fields = ('number', 'description', 'resolution_end_date', 'status', 'assigned_to', 'created_at')
    list_filter = (
        'status', 
        ('created_at', DateRangeFilter),
        ('resolution_end_date', DateRangeFilter),
    )
    list_per_page = 25