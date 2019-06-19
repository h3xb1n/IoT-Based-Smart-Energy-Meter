from django.views.generic import TemplateView, View
from django.db.models import Avg
from django.http import HttpResponse
from .resources import EnergyUsageResource, EnergyUsageResourceMonth
from .models import EnergyUsage
from datetime import date
import calendar

class HomePageView(TemplateView):
    template_name = 'home.html'

class Conv2Excel(View):
    def get(self, request, *args, **kwargs):
        cur_date = date.today()
        energyusage_resource = EnergyUsageResource()
        queryset = EnergyUsage.objects.filter(cdate=date.today())
        dataset = energyusage_resource.export(queryset)
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="' + str(cur_date.day)+'_' + date(1900, cur_date.month, 1).strftime('%B') + "_" + str(cur_date.year)+'.xls"'
        return response
    
class Conv2ExcelMonthly(View):

    def get(self, request, *args, **kwargs):
        energyusage_resource = EnergyUsageResource()
        queryset = EnergyUsage.objects.all()
        month = int(request.GET['month'])
        year = int(request.GET['year'])
        queryset = queryset.filter(cdate__gte=date(year, month, 1))
        queryset = queryset.filter(cdate__lte=date(year, month, calendar.monthrange(year, month)[1]))
#        queryset = queryset.values('cdate').annotate(voltage=Avg('voltage'),current=Avg('current'), watt=Avg('watt'))
        dataset = energyusage_resource.export(queryset)
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="' + date(1900, month, 1).strftime('%B') + "_" + str(year) +'.xls"'
        return response

class Conv2ExcelDaily(View):

    def get(self, request, *args, **kwargs):
        energyusage_resource = EnergyUsageResource()
        queryset = EnergyUsage.objects.all()
        day = int(request.GET['day'])
        month = int(request.GET['month'])
        year = int(request.GET['year'])
        queryset = queryset.filter(cdate=date(year, month, day))
        dataset = energyusage_resource.export(queryset)
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="' + str(day)+'_' + date(1900, month, 1).strftime('%B') + "_" + str(year)+'.xls"'

        return response
