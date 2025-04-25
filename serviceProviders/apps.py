from django.apps import AppConfig
from django.contrib import admin

class ServiceProvidersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'serviceProviders'

    def ready(self):
        admin.site.site_header = 'Seva Enterprises Administration'
        admin.site.site_title = 'Seva Enterprises Admin'
        admin.site.index_title = 'Welcome to Seva Enterprises Administration' 