from django.apps import AppConfig

VERBOSE_APP_NAME = u"帐户管理"
class MyusersConfig(AppConfig):
    name = 'myusers'
    verbose_name = VERBOSE_APP_NAME
