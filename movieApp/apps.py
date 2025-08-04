from django.apps import AppConfig


class MovieappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movieApp'
    def ready(self):
        import movieApp.signals