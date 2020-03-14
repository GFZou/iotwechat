#物联设备状态列表,用于进行查看该设备信息相关信息，建立日期：2020.03.14
from django.db import models

class iot_devicestatusinfo(models.Model):
    deviceinfosn = models.CharField('设备代码',help_text='客户该设备相关特定串号,文本最长30', max_length=30, blank=True)
    deviceportnm = models.CharField('端口名称',help_text='比如说是走廊灯什么的，由客户定义并显示，文本最长30', max_length=30, blank=True)
    deviceport = models.CharField('端口代号',help_text='厂家定义，由设备产生自动写入，不定期更新产品自己的端口，文本最长30', max_length=30, blank=True)

    devicecommand = models.CharField('操作命令',help_text='对应端口的操作，文本最长30', max_length=30, blank=True)
    devicestatus = models.CharField('端口状态',help_text='比如继电器1、0，温湿度为具体值，固定最长30', max_length=30, blank=True)
    deviceopdirect = models.CharField('操作对象',help_text='比如说客户、服务商、设备，固定最长30', max_length=30, blank=True)
    deviceupdate = models.CharField('更新详细时间', help_text='设备状态更新时间，文本最长30', max_length=30, blank=True)

    def __unicode__(self):
        return self.deviceinfosn

    class Meta:
        verbose_name='物联设备状态表'
        verbose_name_plural='物联设备状态列表'
        #'定义设备类型的基本定义，标准几路输入输出，是否已经停产等等'