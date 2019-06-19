from django.db import models
from datetime import date, datetime

class EnergyUsage(models.Model):
    cdate = models.DateField(auto_now_add=True)
    ctime = models.TimeField(auto_now_add=True)
    voltage = models.FloatField(null=False, blank=False)
    current = models.FloatField(null=False, blank=False)
    watt = models.FloatField(null=False, blank=False)
   # cdate = models.datefield(null=false, default=date.today);
   # ctime = models.timefield(null=false, default=datetime.now().time)

    def __str__(self):
        return str(self.id)

