from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_api.auth.accounts'

    def ready(self):
        """
        Docstring for ready
        
        :param self: Description
        In Baraye shenasayee va Ejra Kardane Signal ha estefadeh mishavad !
        
        """
        import drf_api.auth.accounts.signals 