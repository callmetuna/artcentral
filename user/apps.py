from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'userapp'


    def read(self):
        from . import signals
        