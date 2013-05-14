# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.contrib import admin
from django.db import models
        
admin.autodiscover()

class InstanceMonitor(models.Model):
    '''
    virt-top time  16:57:40 Host sns x86_64 4/4CPU 1200MHz 7976MB 
   ID S RDRQ WRRQ RXBY TXBY %CPU %MEM   TIME    NAME
    '''
    uuid=models.CharField(max_length=255, primary_key=True)
    hosttime=models.DateTimeField(null=True,blank=True)
    host=models.CharField(max_length=100)
    rdrq=models.IntegerField()
    wrrq=models.IntegerField()
    txby=models.IntegerField()
    cpu=models.IntegerField()
    mem=models.IntegerField()
    vmtime=models.DateTimeField(null=True,blank=True)
class Service(models.Model):
    name=models.CharField('服务名称',max_length=20)
    code=models.CharField('服务代码',max_length=20,unique=True)
    host=models.IPAddressField('主机地址')
    port=models.IntegerField('端口号')
    version=models.CharField('版本号',max_length=20)
    prefix=models.CharField('url前缀',max_length=200,blank=True)
    
    def __unicode__(self):
        return self.name
class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','code','host','port','version','prefix',)
admin.site.register(Service,ServiceAdmin)    
   
class ApiDoc(models.Model):
    path =models.CharField('访问路径',max_length=200)
    description=models.CharField('说明',max_length=200,blank=True)
    method=models.CharField('http方法',choices=(('GET','GET'),('POST','POST'),('PUT','PUT'),('DELETE','DELETE'),),max_length=20,default='GET')
    path_stack=models.CharField('stack路经',max_length=200)
    service=models.ForeignKey(Service,verbose_name='服务名称')
    #service=models.CharField('服务类型',max_length=20,choices=(('keystone','keystone'),('compute','compute'),('glance','glance'),('volume','volume'),),default='compute')
    component=models.CharField('组件名称',max_length=20)
    req=models.TextField('请求格式',max_length=1000,blank=True)
    resp_success=models.TextField('成功响应格式',max_length=1000,blank=True)
    resp_error=models.TextField('出错响应格式',max_length=1000,blank=True)
    verified=models.BooleanField('是否验证')
    
    def __unicode__(self):
        return self.path
    
    
class ApiDocAdmin(admin.ModelAdmin):
    list_display = ('method','path', 'service','component','description','verified',)
    ordering=('path',)
    list_filter = ('path','service', 'component',)
    search_fields = ['path','component',]
admin.site.register(ApiDoc,ApiDocAdmin)

class Resource(models.Model):
    path =models.CharField('访问路径',max_length=200,unique=True)
    path_stack=models.CharField('stack路经',max_length=200,blank=True,unique=True)
    service=models.ForeignKey(Service,verbose_name='服务名称')
    component=models.CharField('组件名称',max_length=20,blank=True)
    enable=models.BooleanField('是否启用')
    def __unicode__(self):
        return self.path
    
class ResourceAdmin(admin.ModelAdmin):
    list_display=('id','path','path_stack','service','component','enable',)
    ordering=('-id',)
    search_fields=['path','path_stack','component',]
    
admin.site.register(Resource,ResourceAdmin)


class Method(models.Model):
    resource=models.ForeignKey(Resource,verbose_name='资源路径',related_name='resource_method')
    description=models.CharField('说明',max_length=200)
    method=models.CharField('http方法',choices=(('GET','GET'),('POST','POST'),('PUT','PUT'),('DELETE','DELETE'),('HEAD','HEAD'),('PATCH','PATCH'),),max_length=20,default='GET')
    req=models.TextField('请求格式',max_length=1000,blank=True)
    resp=models.TextField('响应格式',max_length=1000,blank=True)
    
    def __unicode__(self):
        return self.description
class MethodAdmin(admin.ModelAdmin):
    list_display=('id','description','resource','method')
    ordering=('-id',)
    list_filter=('resource',)
    search_fields=['description',]
    
admin.site.register(Method,MethodAdmin)

class Error(models.Model):
    resource=models.ForeignKey(Resource,verbose_name='所在资源',related_name='resource_error')
    description=models.CharField('说明',max_length=200,blank=True)
    http_code=models.IntegerField()
    resp=models.TextField('响应格式',max_length=1000,blank=True)
    solution=models.CharField('解决方法',max_length=200,blank=True)
    def __unicode__(self):
        return '%s %s' %(self.id,self.description)
class ErrorAdmin(admin.ModelAdmin):
    list_display=('resource','description')
admin.site.register(Error,ErrorAdmin)    

    