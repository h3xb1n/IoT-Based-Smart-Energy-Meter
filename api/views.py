from django.http import HttpResponse
from django.views.generic import View
from rest_framework import generics
from django.db.models import Avg, Sum
from datetime import date 
from datetime import datetime as dt
import time
import calendar
import json

from pages.models import EnergyUsage
from . import serializers

class ListDate(View):
    def get(self, request, *args, **kwargs):
        time = dt.now()
        cdate = str(time.date().year) + "-" + str(time.date().month) + "-" + str(time.date().day)
        html = "<html><body>%s</body></html>" % cdate
        return HttpResponse(html)


class ListTime(View):
    def get(self, request, *args, **kwargs):
        time = dt.now()
        ctime = str(time.time().hour) + ":" + str(time.time().minute) + ":" + str(time.time().second)
        html = "<html><body>%s</body></html>" % ctime
        return HttpResponse(html)


class ListEnergyUsage(generics.ListCreateAPIView):
    queryset = EnergyUsage.objects.all()
    serializer_class = serializers.EnergyUsageSerializer

class ListEnergyUsageByMonth(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    def get_queryset(self):
        queryset = EnergyUsage.objects.all()
        month = int(self.request.query_params.get('month', None))
        year = int(self.request.query_params.get('year', None))
        queryset = queryset.filter(cdate__gte=date(year, month, 1))
        queryset = queryset.filter(cdate__lte=date(year, month, calendar.monthrange(year, month)[1]))
        queryset = queryset.values('cdate').annotate(voltage=Avg('voltage'),current=Avg('current'), watt=Avg('watt'))
        return queryset

class ListTotalEnergyUsageByMonth(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    queryset = ''

    def list(self, request, *args, **kwargs):
        queryset = EnergyUsage.objects.all()
        month = int(self.request.query_params.get('month', None))
        year = int(self.request.query_params.get('year', None))
        queryset = queryset.filter(cdate__gte=date(year, month, 1))
        queryset = queryset.filter(cdate__lte=date(year, month, calendar.monthrange(year, month)[1]))
        queryset = queryset.aggregate(voltage=Sum('voltage'), current=Sum('current'), watt=Sum('watt'))
        response = super(ListTotalEnergyUsageByMonth, self).list(request, *args, **kwargs)
        response.data = queryset
        return response 

class ListTotalEnergyUsageLive(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    queryset = ''

    def list(self, request, *args, **kwargs):
        #queryset = EnergyUsage.objects.filter(cdate=date(2019,3,17))
        queryset = EnergyUsage.objects.filter(cdate=date.today())
        queryset = queryset.aggregate(voltage=Sum('voltage'), current=Sum('current'), watt=Sum('watt'))
        response = super(ListTotalEnergyUsageLive, self).list(request, *args, **kwargs)
        response.data = queryset
        return response 

class ListEnergyUsageLive(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    def get_queryset(self):
        last_id = int(self.request.query_params.get('last_id', -1))
        if last_id == -1:
            queryset = EnergyUsage.objects.filter(cdate=date.today())
            #queryset = EnergyUsage.objects.filter(cdate=date(2019,3,17))
            if len(queryset) == 0:
                return queryset
            if len(queryset) < 15:
                return queryset
            queryset = queryset[len(queryset)-15:]
        else:
            queryset = EnergyUsage.objects.filter(cdate=date.today())
            #queryset = EnergyUsage.objects.filter(cdate=date(2019,3,17))
            queryset = EnergyUsage.objects.filter(id__gt = last_id)
        #month = int(self.request.query_params.get('month', None))
        #year = int(self.request.query_params.get('year', None))
        #queryset = queryset.filter(cdate=date.today())
       #queryset = queryset.filter(cdate__lte=date(year, month, calendar.monthrange(year, month)[1]))
       # queryset = queryset.values('cdate').annotate(voltage=Avg('voltage'),current=Avg('current'), watt=Avg('watt'))
        return queryset

class ListEnergyUsageByDay(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    def get_queryset(self):
        queryset = EnergyUsage.objects.all()
        day = int(self.request.query_params.get('day', None))
        month = int(self.request.query_params.get('month', None))
        year = int(self.request.query_params.get('year', None))
        queryset = queryset.filter(cdate=date(year, month, day))
        return queryset

class ListTotalEnergyUsageByDay(generics.ListAPIView):
    serializer_class = serializers.EnergyUsageSerializer
    queryset = ''

    def list(self, request, *args, **kwargs):
        queryset = EnergyUsage.objects.all()
        day = int(self.request.query_params.get('day', None))
        month = int(self.request.query_params.get('month', None))
        year = int(self.request.query_params.get('year', None))
        queryset = queryset.filter(cdate=date(year, month, day))
        queryset = queryset.aggregate(voltage=Sum('voltage'), current=Sum('current'), watt=Sum('watt'))
        response = super(ListTotalEnergyUsageByDay, self).list(request, *args, **kwargs)
        response.data = queryset
        return response 

