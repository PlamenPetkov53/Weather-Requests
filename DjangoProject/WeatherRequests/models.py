from django.db import models
from datetime import datetime

# Create your models here.
class RequestedCities(models.Model):
    name_of_city  = models.CharField(max_length=255)
    current_temp  = models.IntegerField()
    current_humidity = models.IntegerField()
    sky_cond = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
