from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Service, ServiceProvider, GlobalSettings

# Register Service Model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_link')
    search_fields = ('name',)

# ServiceProvider Resource for Import/Export
class ServiceProviderResource(resources.ModelResource):
    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, 'name')  # Ensures correct mapping
    )

    class Meta:
        model = ServiceProvider
        fields = ('id', 'name', 'profile_pic', 'description', 'service', 'rating', 
                  'availability', 'experience')
        export_order = ('id', 'name', 'profile_pic', 'description', 'service', 'rating', 
                        'availability', 'experience')

# Register ServiceProvider Model with Import/Export functionality
@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = ServiceProviderResource
    list_display = ('name', 'service', 'rating', 'availability', 'experience')
    list_filter = ('service', 'availability')
    search_fields = ('name', 'description')
    list_editable = ('availability',)

# Register GlobalSettings Model
@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ('service_provider_number',)
