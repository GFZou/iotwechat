# Generated by Django 3.0.4 on 2020-03-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iot_devtype',
            options={'verbose_name': '物联设备类型', 'verbose_name_plural': '物联设备类型表'},
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypecode',
            field=models.CharField(blank=True, help_text='设备类型代码,文本最长30', max_length=30, verbose_name='代码'),
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypeinputnum',
            field=models.CharField(blank=True, help_text='设备输入端口数(整数)，数值最大999', max_length=3, verbose_name='输入'),
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypename',
            field=models.CharField(blank=True, help_text='设备类型名称，文本最长20', max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypeoutputnum',
            field=models.CharField(blank=True, help_text='输出端口数(整数)，数值最大999', max_length=3, verbose_name='输出'),
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypeslug',
            field=models.SlugField(blank=True, help_text='停止生产标志，1或者0', max_length=10, verbose_name='停产'),
        ),
        migrations.AlterField(
            model_name='iot_devtype',
            name='devtypetempsensor',
            field=models.CharField(blank=True, help_text='传感器类型代码，文本最长30', max_length=30, verbose_name='传感器'),
        ),
    ]
