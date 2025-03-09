from rest_framework import serializers
from .models import Service, ServiceProvider

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)  
    global_number = serializers.SerializerMethodField()

    class Meta:
        model = ServiceProvider
        fields = '__all__'  
    
    def get_fields(self):
        fields = super().get_fields()
        fields['global_number'] = serializers.SerializerMethodField()
        return fields
  
    def get_global_number(self, obj):
        return obj.global_number  
