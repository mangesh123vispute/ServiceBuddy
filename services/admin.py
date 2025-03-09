from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Service, ServiceProvider, GlobalSettings
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

# ServiceProvider resource for import/export
class ServiceProviderResource(resources.ModelResource):
    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, 'name')  # Import service by name
    )

    class Meta:
        model = ServiceProvider
        exclude = ('id',)  # Exclude 'id' from import
        import_id_fields = ['name']  # Identify records by 'name' instead of 'id'

# Register Service model with all fields visible
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]  # Show all fields
    search_fields = ('name',)

# Register ServiceProvider model with Import/Export enabled
@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = ServiceProviderResource
    list_display = [field.name for field in ServiceProvider._meta.fields]  # Show all fields
    search_fields = ('name', 'service__name')

# Register GlobalSettings model with all fields visible
@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GlobalSettings._meta.fields]  # Show all fields
