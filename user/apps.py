from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'userapp'


    def ready(self):
        from . import signals
        
