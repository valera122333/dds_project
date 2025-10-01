from django.apps import AppConfig


# Конфигурация приложения "dds"
class DdsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dds"
    verbose_name = "Движение денежных средств"
