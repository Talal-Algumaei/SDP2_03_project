from rest_framework import serializers
from .models import DashPanelData, PrintTrackData

class DashPanelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashPanelData
        fields = '__all__'

class PrintTrackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintTrackData
        fields = '__all__'