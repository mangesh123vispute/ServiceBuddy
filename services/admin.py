from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Service, ServiceProvider, GlobalSettings

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
