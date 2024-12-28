from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Restaurant(models.Model):
    LEAD_STATUS_CHOICES = [
        ('NEW', 'New Lead'),
        ('CONTACTED', 'Contacted'),
        ('MEETING_SCHEDULED', 'Meeting Scheduled'),
        ('NEGOTIATING', 'Negotiating'),
        ('CONVERTED', 'Converted'),
        ('LOST', 'Lost'),
    ]

    name = models.CharField(max_length=200)
    address = models.TextField(null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    lead_status = models.CharField(max_length=20, choices=LEAD_STATUS_CHOICES, default='NEW')
    potential_revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    restaurant_type = models.CharField(max_length=100, null=True, blank=True)
    cuisine_type = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Adding KAM relationship
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='leads')

    def __str__(self):
        return f"{self.name} - {self.get_lead_status_display()}"


class LeadStatusHistory(models.Model):
    lead = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='status_history')
    old_status = models.CharField(max_length=20, choices=Restaurant.LEAD_STATUS_CHOICES)
    new_status = models.CharField(max_length=20, choices=Restaurant.LEAD_STATUS_CHOICES)
    changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead.name}: {self.old_status} -> {self.new_status} at {self.changed_at}"
