# Generated by Django 3.0.4 on 2020-03-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iot_devtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devtypecode', models.CharField(blank=True, help_text='设备类型代码', max_length=30)),
                ('devtypename', models.CharField(blank=True, max_length=20, verbose_name='设备类型名称')),
                ('devtypeinputnum', models.CharField(blank=True, max_length=3, verbose_name='输入端口数')),
                ('devtypeoutputnum', models.CharField(blank=True, max_length=3, verbose_name='输出端口数')),
                ('devtypetempsensor', models.CharField(blank=True, max_length=1, verbose_name='传感器类型代码')),
                ('devtypeslug', models.SlugField(blank=True, max_length=60, verbose_name='停止生产标志')),
            ],
        ),
    ]
