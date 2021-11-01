from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TicketData(models.Model):
    ''' created database fields'''
    topic = models.CharField(max_length=200)
    tower = models.CharField(max_length=200)
    dc = models.CharField(max_length=200)
    action_item = models.CharField(max_length=1000)
    severity = models.CharField(max_length=200)
    action_history = models.CharField(max_length=1000)
    owner = models.CharField(max_length=100)
    eta = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = "ticket_data"


class CompletedTicketData(models.Model):
    ''' created database fields'''
    topic = models.CharField(max_length=200)
    tower = models.CharField(max_length=200)
    dc = models.CharField(max_length=200)
    action_item = models.CharField(max_length=1000)
    severity = models.CharField(max_length=200)
    action_history = models.CharField(max_length=1000)
    owner = models.CharField(max_length=100)
    eta = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = "Completed_ticket_data"

