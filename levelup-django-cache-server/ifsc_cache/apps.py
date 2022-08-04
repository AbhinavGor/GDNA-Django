from django.apps import AppConfig
from numpy import histogram


class IfscCacheConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ifsc_cache'

    def ready(self):
        global hit_count
        hit_count = {}
