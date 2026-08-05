from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default = False ,db_index=True)
    class Meta:
            abstract = True


class User(AbstractUser, TimeStampedModel):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SUPPORT = 'SUPPORT', 'Support'
        CUSTOMER = 'CUSTOMER', 'Customer'

    role = models.CharField(
        max_length=15, 
        choices=Role.choices, 
        default=Role.CUSTOMER
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Department(TimeStampedModel):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100 , unique=True) 
    description = models.TextField(blank=True, null=True)

class Ticket(TimeStampedModel):
    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
    def __str__(self):
        return f"{self.title} - {self.customer.username}"
    title = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department_tickets')
    priority = models.CharField(max_length=10 , choices=Priority.choices , default=Priority.MEDIUM)

class TicketMessage(TimeStampedModel): 
    def __str__(self):
        return f"{self.sender.username}: {self.ticket.title}"
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='messages') 
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_messages')
    message = models.TextField()