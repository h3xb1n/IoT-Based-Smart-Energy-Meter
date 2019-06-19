from django.urls import path

from .views import HomePageView, Conv2Excel, Conv2ExcelMonthly, Conv2ExcelDaily

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('conv2excel/', Conv2Excel.as_view(), name='conv2excel'),
        path('conv2excel/monthly/', Conv2ExcelMonthly.as_view(), name='conv2excel'),
        path('conv2excel/daily/', Conv2ExcelDaily.as_view(), name='conv2excel'),
    ]
