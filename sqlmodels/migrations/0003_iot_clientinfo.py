# Generated by Django 3.0.4 on 2020-03-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmodels', '0002_auto_20200314_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='iot_clientinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientcode', models.CharField(blank=True, help_text='客户相关特定代码,文本最长30', max_length=30, verbose_name='代码')),
                ('clientwechatid', models.CharField(blank=True, help_text='客户微信号，唯一id，文本最长50', max_length=50, verbose_name='微信号')),
                ('clientwechatnm', models.CharField(blank=True, help_text='客户微信呢称，唯一，文本最长30', max_length=30, verbose_name='微信名')),
                ('clientcellphone', models.CharField(blank=True, help_text='客户手机号，文本最长20', max_length=20, verbose_name='手机号')),
                ('clientadress', models.CharField(blank=True, help_text='产品速递地址，文本最长100', max_length=100, verbose_name='邮寄地址')),
                ('clientbinded', models.SlugField(blank=True, help_text='客户是否已经注册绑定标志，1或者0', max_length=10, verbose_name='注册绑定')),
            ],
            options={
                'verbose_name': '客户详细信息',
                'verbose_name_plural': '客户详细信息表',
            },
        ),
    ]
