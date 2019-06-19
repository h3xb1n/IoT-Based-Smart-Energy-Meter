from import_export import resources
from import_export.fields import Field
from .models import EnergyUsage

bill_cost = 4.76

class EnergyUsageResource(resources.ModelResource):
    Date = Field()
    Time = Field()
    Bill = Field()
    Voltage = Field()
    Current = Field()
    Watt = Field()
    
    class Meta:
        model = EnergyUsage
        exclude = ('id,cdate,ctime,voltage,current,watt')
        export_order = ('Date', 'Time', 'Voltage', 'Current', 'Watt','Bill')

    def dehydrate_Voltage(self, EnergyUsage):
        voltage = "%.2f" % (EnergyUsage.voltage)
        return '%s' % (voltage)

    def dehydrate_Current(self, EnergyUsage):
        current = "%.2f" % (EnergyUsage.current)
        return '%s' % (current)

    def dehydrate_Watt(self, EnergyUsage):
        watt = "%.2f" % (EnergyUsage.watt)
        return '%s' % (watt)

    def dehydrate_Date(self, EnergyUsage):
        d = str(EnergyUsage.cdate.day).rjust(2, '0')
        m = str(EnergyUsage.cdate.month).rjust(2, '0')
        y = str(EnergyUsage.cdate.year).rjust(4, '0')

        return '%s-%s-%s' % (d, m, y)

    def dehydrate_Time(self, EnergyUsage):
        hr = str(EnergyUsage.ctime.hour).rjust(2, '0')
        mi = str(EnergyUsage.ctime.minute).rjust(2, '0')
        se = str(EnergyUsage.ctime.second).rjust(2, '0')
        return '%s:%s:%s' % (hr,mi,se) 

    def dehydrate_Bill(self, EnergyUsage):
        bill = "%.4f" % ((EnergyUsage.watt/1000)*bill_cost)
        return '%s' % (bill)

class EnergyUsageResourceMonth(resources.ModelResource):
    Date = Field()
    Time = Field()
    Bill = Field()
    Voltage = Field()
    Current = Field()
    Watt = Field()
    
    class Meta:
        model = EnergyUsage
        exclude = ('id,cdate,ctime,voltage,current,watt')
        export_order = ('Date', 'Time', 'Voltage', 'Current', 'Watt','Bill')

    def dehydrate_Voltage(self, EnergyUsage):
        voltage = "%.2f" % (EnergyUsage.voltage)
        return '%s' % (voltage)

    def dehydrate_Current(self, EnergyUsage):
        current = "%.2f" % (EnergyUsage.current)
        return '%s' % (current)

    def dehydrate_Watt(self, EnergyUsage):
        watt = "%.2f" % (EnergyUsage.watt)
        return '%s' % (watt)

    def dehydrate_Date(self, EnergyUsage):
        d = str(EnergyUsage.cdate.day).rjust(2, '0')
        m = str(EnergyUsage.cdate.month).rjust(2, '0')
        y = str(EnergyUsage.cdate.year).rjust(4, '0')
        return '%s-%s-%s' % (d, m, y)

    def dehydrate_Time(self, EnergyUsage):
        hr = str(EnergyUsage.ctime.hour).rjust(2, '0')
        mi = str(EnergyUsage.ctime.minute).rjust(2, '0')
        se = str(EnergyUsage.ctime.second).rjust(2, '0')
        return '%s:%s:%s' % (hr,mi,se) 

    def dehydrate_Bill(self, EnergyUsage):
        bill = "%.4f" % ((EnergyUsage.watt/1000)*bill_cost)
        return '%s' % (bill)
