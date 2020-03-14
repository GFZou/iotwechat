from django.apps import AppConfig


class SqlmodelsConfig(AppConfig):
    name = 'sqlmodels'

    class Meta:
    #    db_table = 'iot_devtype'  # 通过db_table自定义数据表名
        verbose_name='数据表'
        verbose_name_plural='数据库结构'
