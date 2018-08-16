from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'
    label='红酒追溯管理'
    verbose_name = "红酒追溯管理"
    verbose_name_plural = verbose_name

    class Meta:
        verbose_name = "红酒追溯管理"
        label='红酒追溯管理'
        verbose_name_plural = verbose_name
