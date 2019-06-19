from rest_framework import serializers
from pages.models import EnergyUsage

class EnergyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'current', 'voltage', 'watt', 'cdate', 'ctime',)
        model = EnergyUsage
