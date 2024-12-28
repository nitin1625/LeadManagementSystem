from django.db import models
from django.utils import timezone
from leads.models import Restaurant  # Assuming Restaurant is in your 'leads' app

class CallPlan(models.Model):
    FREQUENCY_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('BIWEEKLY', 'Bi-Weekly'),
        ('MONTHLY', 'Monthly')
    ]

    lead = models.OneToOneField(Restaurant, on_delete=models.CASCADE,default=1)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='DAILY')
    last_called = models.DateTimeField(null=True, blank=True)
    next_call_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    def update_next_call(self):
        """Updates the next call date based on the frequency"""
        if self.last_called:
            if self.frequency == 'DAILY':
                self.next_call_date = self.last_called + timezone.timedelta(days=1)
            elif self.frequency == 'WEEKLY':
                self.next_call_date = self.last_called + timezone.timedelta(weeks=1)
            elif self.frequency == 'BIWEEKLY':
                self.next_call_date = self.last_called + timezone.timedelta(weeks=2)
            elif self.frequency == 'MONTHLY':
                self.next_call_date = self.last_called + timezone.timedelta(days=30)
        self.save()

