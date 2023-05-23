import random
import string

from django.db import models
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    number = models.CharField(max_length=100, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True, editable=False)
    resolution_end_date = models.DateField()
    assigned_to = models.ForeignKey("employee.Employee", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.number
    
    @staticmethod
    def generate_ticket_number(code):
        # e.g. 230105-ABC
        abc = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
        return f"{code}-{abc}"
    
    def save(self, *args, **kwargs):
        if not self.number:
            today = timezone.now().strftime("%y%m%d")
            # Generate number once, then check the db. If exists, keep trying.
            self.number = self.generate_ticket_number(today)
            while Ticket.objects.filter(number=self.number).exists():
                self.number = self.generate_ticket_number(today)
        return super().save(*args, **kwargs)