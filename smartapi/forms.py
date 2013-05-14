# -*- encoding=utf8 -*-
'''
Created on 2012-12-11

@author: lion
'''
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from smartapi.stack import getToken
import logging

class LogonForm(forms.Form):
    username = forms.CharField(max_length=200, label=u'用户名',initial='')
    password = forms.CharField(label=u'密码',
                             widget=forms.PasswordInput(),initial=''
                             )
    tenantid = forms.CharField(max_length=200, label=u'租户ID',initial='')
    openstack_url= forms.CharField(max_length=200,label=u'Openstack Keystone服务器IP:',initial="")
    
    def validate(self):
        cd=self.cleaned_data
        return getToken(cd['username'],cd['password'],cd['tenantid'],cd['openstack_url'])

class ApiAuthForm(forms.Form):
    username = forms.CharField(max_length=200, label=u'用户名',initial='admin')
    password = forms.CharField(label=u'密码',
                             widget=forms.PasswordInput(),initial='password'
                             )
    
    def validate(self):
        cd=self.cleaned_data
        return getToken(cd['username'],cd['password'],cd['tenantid'])   
class CreateServerForm(forms.Form):
    server_name = forms.CharField(max_length=200, label=u'服务器名称',initial='')
    image_id = forms.CharField(max_length=200, label=u'镜像ID',initial='')
    flavor_id= forms.CharField(max_length=200, label=u'类型ID',initial='')
    server_count = forms.IntegerField(label=u'服务器数量')

    