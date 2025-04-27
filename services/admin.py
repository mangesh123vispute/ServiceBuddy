from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Service, ServiceProvider, GlobalSettings, CustomerRequest, Comments
from django.utils import timezone
class ServiceProviderResource(resources.ModelResource):
    services = fields.Field(
        column_name='services',
        attribute='services',
        widget=ForeignKeyWidget(Service, field='id')
    )

    class Meta:
        model = ServiceProvider
        fields = ('id', 'name', 'description', 'services', 'rating', 'availability', 'experience')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = ServiceProviderResource
    list_display = ('id', 'name', 'get_services', 'rating', 'availability', 'experience')
    search_fields = ('name', 'services__name')
    list_filter = ('availability', 'services')
    filter_horizontal = ('services',)

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services'

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = ('id', 'name', 'icon_link')

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = ('id', 'name', 'order', 'icon_link')
    search_fields = ('name',)
    list_editable = ('order',)

@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ('id','service_provider_number',)

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'mobile_number', 'preferred_time_slot', 'delivery_date', 'formatted_timestamp', 'completed')
    list_filter = ('completed', 'service', 'timestamp')
    search_fields = ('name', 'mobile_number', 'address', 'service__name')
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    
    def formatted_timestamp(self, obj):
        return timezone.localtime(obj.timestamp).strftime('%d %b %Y, %I:%M %p')
    formatted_timestamp.short_description = 'Request Time'
    formatted_timestamp.admin_order_field = 'timestamp'
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'mobile_number', 'address')
        }),
        ('Service Details', {
            'fields': ('service', 'preferred_time_slot', 'delivery_date')
        }),
        ('Status', {
            'fields': ('completed', 'timestamp')
        }),
    )

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_provider', 'service', 'service_receiver_name', 'formatted_timestamp', 'comment')
    list_filter = ('service_provider', 'service', 'timestamp')
    search_fields = ('service_receiver_name', 'comment', 'service_provider__name', 'service__name')
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    
    def formatted_timestamp(self, obj):
        return timezone.localtime(obj.timestamp).strftime('%d %b %Y, %I:%M %p')
    formatted_timestamp.short_description = 'Comment Time (IST)'
    formatted_timestamp.admin_order_field = 'timestamp'
