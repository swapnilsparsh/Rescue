from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'
    def ready(self):
        import main_app.signals