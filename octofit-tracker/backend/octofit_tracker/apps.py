from django.apps import AppConfig
from django.db.models.signals import post_migrate

def disable_post_migrate_signal(*args, **kwargs):
    # Disable the post_migrate signal globally
    pass

class OctofitTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'octofit_tracker'

    def ready(self):
        post_migrate.disconnect(dispatch_uid='django.contrib.auth.management.create_permissions')
        post_migrate.connect(disable_post_migrate_signal, dispatch_uid='disable_post_migrate_signal')
