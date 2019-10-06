from django.db import models
from app_client.models import Client
from app_sw.models import Service

# Create your models here.
class Date(models.Model):
    #pre-pay,payed,started,ended,timed out
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    PAYED = 'payed'
    STARTED = 'started'
    ENDED = 'ended'
    TIMEDOUT='timed out'
    STATE_CHOICES = [
        (REQUESTED , 'requested'),
        (ACCEPTED, 'accepted'),
        (PAYED , 'payed'),
        (STARTED , 'started'),
        (ENDED , 'ended'),
        (TIMEDOUT , 'timed out'),
    ]
    client=models.OneToOneField(Client,on_delete=models.CASCADE)
    service=models.OneToOneField(Service,on_delete=models.CASCADE)
    start=models.DateTimeField('start time')
    end=models.DateTimeField('end time')
    lat = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    lng = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    state=models.CharField(max_length=20,choices=STATE_CHOICES,default=REQUESTED)
