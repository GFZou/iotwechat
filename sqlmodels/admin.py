from django.contrib import admin

# Register your models here.
from sqlmodels.models import iot_devtype
#class TagInline(admin.TabularInline):
#    model = iot_devtype
#设备类型信息表
class iot_devtypeAdmin(admin.ModelAdmin):
    list_display = ('devtypecode', 'devtypename', 'devtypeinputnum','devtypeoutputnum','devtypehwver',
                    'devicetyperelay','devicetypebattary','devtypenetwork','devtypewifi','devtypenbt','devtypeT_H',
                    'devtypeGPS','devtypeLED','devtypePower','devtypePowernum','devtypetempsensor',
                    'devtypeslug')  # list

    search_fields = ('devtypecode',)
    #inlines = [TagInline]  # Inline
    fieldsets = (
        ['必要信息', {
            'fields': ('devtypecode', 'devtypename', 'devtypeinputnum','devtypeoutputnum','devtypehwver',
                       'devicetyperelay','devicetypebattary','devtypetempsensor'),
        }],
        ['其他附加信息', {
            'classes': ('collapse',),
            'fields': ('devtypenetwork','devtypewifi','devtypenbt','devtypeT_H','devtypeGPS','devtypeLED',
                    'devtypePower','devtypePowernum','devtypeslug'),
        }]
    )
admin.site.register(iot_devtype,iot_devtypeAdmin)

#客户详细信息表
from sqlmodels.clientinfo.clientinfo import iot_clientinfo
class iot_clientinfoAdmin(admin.ModelAdmin):
    list_display = ('clientcode', 'clientwechatid', 'clientwechatnm','clientcellphone','clientadress','clientbinded')  # list
    search_fields = ('clientwechatnm','clientcellphone')

admin.site.register(iot_clientinfo, iot_clientinfoAdmin)

#客户设备详细信息列表
from sqlmodels.clientinfo.clientdevices import iot_clientdevice
class iot_clientdeviceAdmin(admin.ModelAdmin):
    list_display = ('clientdevsn', 'clientdevver', 'clientdevtype','clientwechatid','clientbinddate','clientdevbinded'
                    ,'clientdevarea','clientdevgroup')  # list
    search_fields = ('clientdevsn',)

admin.site.register(iot_clientdevice, iot_clientdeviceAdmin)


#现有设备详细信息
from sqlmodels.deviceinfodetails import iot_deviceinfodetails
class iot_deviceinfodetailsAdmin(admin.ModelAdmin):
    list_display = ('deviceinfosn', 'deviceinfover', 'deviceinforelay','deviceinfobatch','deviceinfotype','deviceinfopfacdate',
                    'deviceinfooutdate','deviceinfosaledate','deviceinfophonesn','deviceinfoexpire','deviceinfoinuse')  # list
    search_fields = ('deviceinfosn',)
admin.site.register(iot_deviceinfodetails, iot_deviceinfodetailsAdmin)

#物联设备状态列表
from sqlmodels.devicestatusinfo import iot_devicestatusinfo
class iot_devicestatusinfoAdmin(admin.ModelAdmin):
    list_display = ('deviceinfosn', 'deviceportnm', 'deviceport','devicecommand','devicestatus','deviceopdirect','deviceupdate')  # list
    search_fields = ('deviceinfosn','deviceportnm')
admin.site.register(iot_devicestatusinfo, iot_devicestatusinfoAdmin)