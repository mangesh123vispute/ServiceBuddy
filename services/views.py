from rest_framework.response import Response
from rest_framework import generics
from .models import Service, ServiceProvider
from .serializers import ServiceSerializer, ServiceProviderSerializer

# 1. /services - Get all services
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# 2. /services/<int:id>/ - Get service providers for a service
class ServiceProviderListView(generics.ListAPIView):
    serializer_class = ServiceProviderSerializer

    def get_queryset(self):
        service_id = self.kwargs['id']
        return ServiceProvider.objects.filter(service_id=service_id)

# 3. /service/<int:service_id>/<int:provider_id>/ - Get details of a specific service provider
class ServiceProviderDetailView(generics.RetrieveAPIView):
    serializer_class = ServiceProviderSerializer

    def get_object(self):
        service_id = self.kwargs.get("service_id")
        provider_id = self.kwargs.get("service_provider_id")

        return ServiceProvider.objects.get(id=provider_id, service_id=service_id)