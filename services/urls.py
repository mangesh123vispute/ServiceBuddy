from django.urls import path
from .views import ServiceListView, ServiceProviderListView, ServiceProviderDetailView, CustomerRequestCreateView, CommentsCreateView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<str:service_name>/', ServiceProviderListView.as_view(), name='service-provider-list'),
    path('services/<str:service_name>/<int:service_provider_id>/', ServiceProviderDetailView.as_view(), name='service-provider-detail'),
    path('customer-request/', CustomerRequestCreateView.as_view(), name='customer-request-create'),
    path('comments/', CommentsCreateView.as_view(), name='comments-create'),
]
