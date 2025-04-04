from django.apps import AppConfig


class JelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jelapp'

    def ready(self):
        # Távolítsd el a signals importot, ha nem használsz signalokat
        pass