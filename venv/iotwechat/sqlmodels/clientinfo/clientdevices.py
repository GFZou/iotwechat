#客户设备详细信息列表,用于前端客户进行查看相关信息，建立日期：2020.03.14
from django.db import models

class iot_clientdevice(models.Model):
    clientdevsn = models.CharField('设备代码',help_text='客户该设备相关特定串号,文本最长30', max_length=30, blank=True)
    clientdevver = models.CharField('固件版本',help_text='现有固件版本，以备查询文本最长30', max_length=30, blank=True)
    clientdevtype = models.CharField('设备类型', help_text='设备类型代码，用于匹配是否需要服务，文本最长50', max_length=50, blank=True)
    clientwechatid = models.CharField('微信号',help_text='客户微信号，唯一id，文本最长50', max_length=50, blank=True)
    clientbinddate = models.CharField('绑定日期',help_text='产品的绑定日期，文本最长100', max_length=100, blank=True)
    clientdevbinded = models.SlugField('注册绑定', help_text='客户是否已经注册绑定标志，1或者0',max_length=10, blank=True)
    clientdevarea = models.CharField('区域划分', help_text='客户自身对设备所在区域的划分',max_length=30, blank=True)
    clientdevgroup = models.CharField('分组划分', help_text='客户自身对设备所在组的划分',max_length=30, blank=True)



    # 通过db_column自定义数据表中字段名
    # title = models.CharField('标题', max_length=200, db_column='article_title')
    # 使用db_index=True对title建立索引
    # title = models.CharField('标题', max_length=200, db_index=True)

    def __unicode__(self):
        return self.clientdevsn

    class Meta:
    #    db_table = 'iot_devtype'  # 通过db_table自定义数据表名
        verbose_name='客户设备详细信息'
        verbose_name_plural='客户绑定设备详细信息列表'
        #'定义设备类型的基本定义，标准几路输入输出，是否已经停产等等'