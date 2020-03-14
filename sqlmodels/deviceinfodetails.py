#设备详细信息列表,用于进行查看该设备信息相关信息，建立日期：2020.03.14
from django.db import models

class iot_deviceinfodetails(models.Model):
    deviceinfosn = models.CharField('设备代码',help_text='客户该设备相关特定串号,文本最长30', max_length=30, blank=True)
    deviceinfover = models.CharField('出厂固件版本',help_text='出厂固件版本，文本最长30', max_length=30, blank=True)
    deviceinforelay = models.CharField('输出命令前缀',help_text='继电器命令前缀，固定最长7', max_length=7, blank=True)
    deviceinfobatch = models.CharField('生产批次号',help_text='设备出厂批次号，固定最长7', max_length=7, blank=True)
    deviceinfotype = models.CharField('设备类型', help_text='设备类型代码，用于匹配是否需要服务，文本最长50', max_length=50, blank=True)
    deviceinfopfacdate = models.CharField('生产日期', help_text='设备的生产日期，文本最长30', max_length=30, blank=True)
    deviceinfooutdate = models.CharField('出厂日期', help_text='设备出厂日期，文本最长30', max_length=30, blank=True)
    deviceinfosaledate = models.CharField('销售日期', help_text='设备销售日期，文本最长30', max_length=30, blank=True)
    deviceinfophonesn = models.CharField('物联卡串号', help_text='出厂时配套的物联卡串号，用于为客户流量服务期的问题，文本最长30', max_length=30, blank=True)
    deviceinfoexpire = models.CharField('服务到期日', help_text='出厂时配套的物联卡到期日，用于为客户流量服务期的问题，文本最长30', max_length=30, blank=True)
    deviceinfoinuse=models.SlugField('是否已报废', help_text='该设备是否已报废，用于厂家自我管控用途，1或者0',max_length=10, blank=True)

    def __unicode__(self):
        return self.deviceinfosn

    class Meta:
        verbose_name='现有设备详细信息'
        verbose_name_plural='物联设备详细信息列表'
        #'定义设备类型的基本定义，标准几路输入输出，是否已经停产等等'