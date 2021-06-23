from django.apps import AppConfig


class AiwebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AIweb'


    def ready(self):
        import AIweb.signals
