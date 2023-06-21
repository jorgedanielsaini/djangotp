from django.apps import AppConfig


class PublicaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'publica'

    def ready(self):
        import publica.signals
