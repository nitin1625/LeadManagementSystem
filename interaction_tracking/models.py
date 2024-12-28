from django.db import models
from leads.models import Restaurant  # Adjust based on your project structure
from contact.models import Contact


class Interaction(models.Model):
    lead = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="interactions")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="interactions")
    interaction_type = models.CharField(max_length=50, choices=[("CALL", "Call"), ("EMAIL", "Email"), ("ORDER", "Order")])
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    order_placed = models.BooleanField(default=False)  # New field

    def __str__(self):
        return f"{self.interaction_type} with {self.contact.name} ({self.lead.name}) on {self.date}"

class Order(models.Model):
    interaction = models.OneToOneField(Interaction, on_delete=models.CASCADE, related_name="order")
    product_details = models.TextField()  # Details about the products
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.interaction.lead.name} on {self.order_date}"