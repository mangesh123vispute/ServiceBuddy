from django.urls import path
from .views import ServiceListView, ServiceProviderListView, ServiceProviderDetailView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:id>/', ServiceProviderListView.as_view(), name='service-provider-list'),
    path('services/<int:service_id>/<int:service_provider_id>/', ServiceProviderDetailView.as_view(), name='service-provider-detail'),
]
