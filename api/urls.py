from django.urls import path

from .views import ListEnergyUsage, ListEnergyUsageByDay, ListEnergyUsageByMonth, ListEnergyUsageLive, ListTotalEnergyUsageByDay, ListTotalEnergyUsageByMonth, ListTotalEnergyUsageLive, ListDate, ListTime

urlpatterns = [
    path('', ListEnergyUsage.as_view()),
    path('daily/total/', ListTotalEnergyUsageByDay.as_view()),
    path('daily/', ListEnergyUsageByDay.as_view()),
    path('monthly/total/', ListTotalEnergyUsageByMonth.as_view()),
    path('monthly/', ListEnergyUsageByMonth.as_view()),
    path('live/', ListEnergyUsageLive.as_view()),
    path('live/total/', ListTotalEnergyUsageLive.as_view()),
    path('date/', ListDate.as_view()),
    path('time/', ListTime.as_view()),
]
