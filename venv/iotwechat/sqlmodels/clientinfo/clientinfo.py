#客户详细信息表,建立日期：2020.03.14
from django.db import models

class iot_clientinfo(models.Model):
    clientcode = models.CharField('代码',help_text='客户相关特定代码,文本最长30', max_length=30, blank=True)
    clientwechatid = models.CharField('微信号',help_text='客户微信号，唯一id，文本最长50', max_length=50, blank=True)
    clientwechatnm = models.CharField('微信名',help_text='客户微信呢称，唯一，文本最长30', max_length=30, blank=True)
    clientcellphone = models.CharField('手机号',help_text='客户手机号，文本最长20', max_length=20, blank=True)
    clientadress = models.CharField('邮寄地址',help_text='产品速递地址，文本最长100', max_length=100, blank=True)
    clientbinded = models.SlugField('注册绑定', help_text='客户是否已经注册绑定标志，1或者0',max_length=10, blank=True)

    # 通过db_column自定义数据表中字段名
    # title = models.CharField('标题', max_length=200, db_column='article_title')
    # 使用db_index=True对title建立索引
    # title = models.CharField('标题', max_length=200, db_index=True)

    def __unicode__(self):
        return self.clientcode

    class Meta:
    #    db_table = 'iot_devtype'  # 通过db_table自定义数据表名
        verbose_name='客户详细信息'
        verbose_name_plural='客户详细信息表'
        #'定义设备类型的基本定义，标准几路输入输出，是否已经停产等等'