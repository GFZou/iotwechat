# Generated by Django 3.0.4 on 2020-03-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmodels', '0003_iot_clientinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='iot_clientdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientdevsn', models.CharField(blank=True, help_text='客户该设备相关特定串号,文本最长30', max_length=30, verbose_name='设备代码')),
                ('clientdevver', models.CharField(blank=True, help_text='现有固件版本，以备查询文本最长30', max_length=30, verbose_name='固件版本')),
                ('clientdevtype', models.CharField(blank=True, help_text='设备类型代码，用于匹配是否需要服务，文本最长50', max_length=50, verbose_name='设备类型')),
                ('clientwechatid', models.CharField(blank=True, help_text='客户微信号，唯一id，文本最长50', max_length=50, verbose_name='微信号')),
                ('clientbinddate', models.CharField(blank=True, help_text='产品的绑定日期，文本最长100', max_length=100, verbose_name='绑定日期')),
                ('clientdevbinded', models.SlugField(blank=True, help_text='客户是否已经注册绑定标志，1或者0', max_length=10, verbose_name='注册绑定')),
            ],
            options={
                'verbose_name': '客户设备详细信息',
                'verbose_name_plural': '客户设备详细信息列表',
            },
        ),
        migrations.CreateModel(
            name='iot_deviceinfodetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceinfosn', models.CharField(blank=True, help_text='客户该设备相关特定串号,文本最长30', max_length=30, verbose_name='设备代码')),
                ('deviceinfover', models.CharField(blank=True, help_text='出厂固件版本，文本最长30', max_length=30, verbose_name='出厂固件版本')),
                ('deviceinfotype', models.CharField(blank=True, help_text='设备类型代码，用于匹配是否需要服务，文本最长50', max_length=50, verbose_name='设备类型')),
                ('deviceinfopfacdate', models.CharField(blank=True, help_text='设备的生产日期，文本最长30', max_length=30, verbose_name='生产日期')),
                ('deviceinfooutdate', models.CharField(blank=True, help_text='设备出厂日期，文本最长30', max_length=30, verbose_name='出厂日期')),
                ('deviceinfosaledate', models.CharField(blank=True, help_text='设备销售日期，文本最长30', max_length=30, verbose_name='销售日期')),
                ('deviceinfophonesn', models.CharField(blank=True, help_text='出厂时配套的物联卡串号，用于为客户流量服务期的问题，文本最长30', max_length=30, verbose_name='物联卡串号')),
                ('deviceinfoexpire', models.CharField(blank=True, help_text='出厂时配套的物联卡到期日，用于为客户流量服务期的问题，文本最长30', max_length=30, verbose_name='服务到期日')),
                ('deviceinfoinuse', models.SlugField(blank=True, help_text='该设备是否已报废，用于厂家自我管控用途，1或者0', max_length=10, verbose_name='是否已报废')),
            ],
            options={
                'verbose_name': '现有设备详细信息',
                'verbose_name_plural': '设备详细信息列表',
            },
        ),
        migrations.AddField(
            model_name='iot_devtype',
            name='devtypehwver',
            field=models.CharField(blank=True, help_text='固件的最新版本号，以便客户可以判定是否需要更新，最长30', max_length=30, verbose_name='固件版本号'),
        ),
    ]
