from rest_framework import serializers
from .models import Service, ServiceProvider

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id', 'profile_pic', 'name', 'description', 'service', 'rating', 'availability', 'experience', 'global_number']

    def get_global_number(self, obj):
        return obj.global_number  
