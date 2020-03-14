# Generated by Django 3.0.4 on 2020-03-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmodels', '0009_iot_devtype_devicetypebattary'),
    ]

    operations = [
        migrations.CreateModel(
            name='iot_devicestatusinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceinfosn', models.CharField(blank=True, help_text='客户该设备相关特定串号,文本最长30', max_length=30, verbose_name='设备代码')),
                ('deviceportnm', models.CharField(blank=True, help_text='比如说是走廊灯什么的，由客户定义并显示，文本最长30', max_length=30, verbose_name='端口名称')),
                ('deviceport', models.CharField(blank=True, help_text='厂家定义，由设备产生自动写入，不定期更新产品自己的端口，文本最长30', max_length=30, verbose_name='端口代号')),
                ('devicecommand', models.CharField(blank=True, help_text='对应端口的操作，文本最长30', max_length=30, verbose_name='操作命令')),
                ('devicestatus', models.CharField(blank=True, help_text='比如继电器1、0，温湿度为具体值，固定最长30', max_length=30, verbose_name='端口状态')),
                ('deviceopdirect', models.CharField(blank=True, help_text='比如说客户、服务商、设备，固定最长30', max_length=30, verbose_name='操作对象')),
                ('deviceupdate', models.CharField(blank=True, help_text='设备状态更新时间，文本最长30', max_length=30, verbose_name='更新详细时间')),
            ],
            options={
                'verbose_name': '物联设备状态表',
                'verbose_name_plural': '物联设备状态列表',
            },
        ),
        migrations.AlterModelOptions(
            name='iot_clientdevice',
            options={'verbose_name': '客户设备详细信息', 'verbose_name_plural': '客户绑定设备详细信息列表'},
        ),
        migrations.AlterModelOptions(
            name='iot_deviceinfodetails',
            options={'verbose_name': '现有设备详细信息', 'verbose_name_plural': '物联设备详细信息列表'},
        ),
    ]