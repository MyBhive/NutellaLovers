from django.apps import AppConfig


class AccountConfig(AppConfig):
    """
    Give a name to my app to create a shortcut for the settings
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
