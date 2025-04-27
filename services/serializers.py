from rest_framework import serializers
from .models import Service, ServiceProvider, CustomerRequest

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    services = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    global_number = serializers.SerializerMethodField()

    class Meta:
        model = ServiceProvider
        fields = ['id', 'profile_pic', 'name', 'description', 'services', 'rating', 'availability', 'experience', 'global_number']

    def get_global_number(self, obj):
        return obj.global_number  

class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = ['id', 'name', 'mobile_number', 'service', 'address', 'preferred_time_slot', 'delivery_date', 'timestamp', 'completed']
        read_only_fields = ['timestamp', 'completed']  