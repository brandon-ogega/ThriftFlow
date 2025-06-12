from django.apps import AppConfig


class ThriftflowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ThriftFlow'

def ready(self):
    import ThriftFlow.signals