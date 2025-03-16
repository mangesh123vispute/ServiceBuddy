from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Service, ServiceProvider, GlobalSettings
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget

# ServiceProvider resource for import/export
class ServiceProviderResource(resources.ModelResource):
    id = fields.Field(
        column_name='id',
        attribute='id',
        widgets=[fields.widgets.IntegerWidget()],
        saves_null_values=False
    )
    
    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, 'name')
    )

    availability = fields.Field(
        column_name='availability',
        attribute='availability',
        widget=BooleanWidget()
    )

    rating = fields.Field(
        column_name='rating',
        attribute='rating',
        widget=fields.widgets.FloatWidget(),
        default=0.0
    )

    experience = fields.Field(
        column_name='experience',
        attribute='experience',
        widget=fields.widgets.FloatWidget(),
        default=0.0
    )

    class Meta:
        model = ServiceProvider
        import_id_fields = ['id']  # Use ID for updating existing records
        fields = ('id', 'name', 'profile_pic', 'description', 'service', 'rating', 'availability', 'experience')
        export_order = fields
        skip_unchanged = True
        report_skipped = True
        exclude = ()

    def before_import_row(self, row, **kwargs):
        # If id is empty or None, remove it to allow auto-generation
        if not row.get('id'):
            row['id'] = None

# Register Service model with all fields visible
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    search_fields = ('name',)

# Register ServiceProvider model with Import/Export enabled
@admin.register(ServiceProvider)
class ServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = ServiceProviderResource
    list_display = ('id', 'name', 'service', 'rating', 'availability', 'experience')
    list_filter = ('service', 'availability')
    search_fields = ('name', 'service__name')
    list_per_page = 25  # Number of items per page
    ordering = ('id',)  # Default ordering

    def get_export_filename(self, request, queryset, file_format):
        return f'service_providers.{file_format.get_extension()}'

# Register GlobalSettings model with all fields visible
@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GlobalSettings._meta.fields]
