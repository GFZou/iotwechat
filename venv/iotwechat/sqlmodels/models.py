#物联设备类型表，建立日期：2020.03.14
from django.db import models

# Create your models here.

class iot_devtype(models.Model):
    devtypecode = models.CharField('代码',help_text='设备类型代码,文本最长30', max_length=30, blank=True)
    devtypename = models.CharField('名称',help_text='设备类型名称，文本最长20', max_length=20, blank=True)
    devtypeinputnum = models.CharField('输入',help_text='设备输入端口数(整数)，数值最大999', max_length=3, blank=True)
    devtypeoutputnum = models.CharField('输出',help_text='输出端口数(整数)，数值最大999', max_length=3, blank=True)
    devtypehwver = models.CharField('固件版本号',help_text='固件的最新版本号，以便客户可以判定是否需要更新，最长30', max_length=30, blank=True)
    devicetyperelay = models.CharField('输出命令前缀',help_text='继电器命令前缀，固定最长7', max_length=7, blank=True)
    devicetypebattary = models.CharField('设备电池容量',help_text='装备该设备的电池容量说明，固定最长30', max_length=30, blank=True)

    devtypenetwork=models.CharField('网络制式',help_text='2G、3G、4G、5G，最长30', max_length=30, blank=True)
    devtypewifi=models.CharField('无线模块',help_text='WIFI标准，没有可空，最长30', max_length=30, blank=True)
    devtypenbt=models.CharField('蓝牙版本',help_text='2.0、3.0、4.0、5.0，可空，最长30', max_length=30, blank=True)
    devtypeT_H=models.CharField('温湿度模块',help_text='元件的标准名称，比如AM2120，最长30', max_length=30, blank=True)
    devtypeGPS=models.CharField('GPS制式',help_text='比如北斗、伽利略、美国GPS，最长30', max_length=30, blank=True)
    devtypeLED=models.CharField('屏幕大小',help_text='屏幕的详细描述，如LED128*64，最长30', max_length=30, blank=True)
    devtypePower=models.CharField('电能检测',help_text='电能测试模块描述，最长30', max_length=30, blank=True)
    devtypePowernum=models.CharField('电能检测数',help_text='电能测试模块几路登记数，最大999', max_length=3, blank=True)

    devtypetempsensor = models.CharField('其他内容说明',help_text='其他内容说明描述，文本最长100', max_length=30, blank=True)
    devtypeslug = models.SlugField('停产', help_text='停止生产标志，1或者0',max_length=10, blank=True)

    # 通过db_column自定义数据表中字段名
    # title = models.CharField('标题', max_length=200, db_column='article_title')
    # 使用db_index=True对title建立索引
    # title = models.CharField('标题', max_length=200, db_index=True)

    def __unicode__(self):
        return self.devtypecode

    class Meta:
    #    db_table = 'iot_devtype'  # 通过db_table自定义数据表名
        verbose_name='物联设备类型'
        verbose_name_plural='物联设备类型表'
        #'定义设备类型的基本定义，标准几路输入输出，是否已经停产等等'
