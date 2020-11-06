from rest_framework import serializers
from .models import PrintFile

class PrintFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintFile
        fields = '__all__'
