from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TicketData(models.Model):
    ''' created database fields'''
    name = models.CharField(max_length=200)
    past_address = models.CharField(max_length=200)
    present_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ticket_data"

