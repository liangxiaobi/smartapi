# -*- encoding=utf8 -*-
'''
Created on 2012-12-11

@author: lion
'''

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import context
from django.template.context import RequestContext
from smartapi.forms import CreateServerForm, LogonForm
from smartapi.models import ApiDoc, Service, Resource
from smartapi.novamodel import Instances, InstanceInfoCaches
from smartapi.stack import getTenantID, stackclient, getToken, getImageList, \
    getFlavorList, createServer, getServerList, deleteServer, restclient
from smartapi.tools import getXmlValue, l, haskeys, render2json, render2html
import json
from datetime import datetime
import os
import random

def home(request):
    if "sess_token" not in request.COOKIES or request.COOKIES["sess_token"]=="":
        return logon(request)
    create_server_form = CreateServerForm();
    context = RequestContext(request, {
             'create_server_form':create_server_form,
             })
    
    return render_to_response('home.html', context)
def kvm(request):
    return render2html("hello world")
def logon(request):
    if request.method == 'POST':
        form = LogonForm(request.POST)
        if form.is_valid():
            service = form.validate()
            print service
            if service:
                cd = form.cleaned_data
                re = HttpResponseRedirect('/')
                expire_datetime=datetime.strptime(service['expire'],"%Y-%m-%dT%H:%M:%SZ")
                #expire_datetime=time.mktime(time.strptime("2013-05-22T03:03:03Z","%Y-%m-%dT%H:%M:%SZ"))
                re.set_cookie('sess_user', cd['username'])  
                re.set_cookie('sess_token', service['token'],expires=expire_datetime)
                re.set_cookie('sess_token_expires', expire_datetime)
                re.set_cookie('sess_service', service)
                re.set_cookie('sess_openstack_url', cd['openstack_url'])
                re.set_cookie("sess_tenant_id",service['tenantid'])
                return re
            else:
                form = LogonForm()
                # form['password'].errors.put("error")
    else:
        form = LogonForm()
    context = RequestContext(request, {'form':form})
    return render_to_response('logon.html', context)
def logout(request):
    re = HttpResponseRedirect('/')
    re.delete_cookie('sess_user')
    re.delete_cookie('sess_token')
    re.delete_cookie('sess_openstack_url') 
    return re
def monitor(request):
    uuid=request.GET.get('uuid','')
    if request.method=='GET' and len(uuid)>10:
#        states=monitorService.readMonitorFile()
#        logging.debug(states)
#        vmstate=states[uuid]
#        vcpu=vmstate[6]
#        mem=vmstate[7]
#        disk=50
#        netin=vmstate[4]
#        netout=vmstate[5]
        
        vcpu=random.randint(1,20)
        mem=random.randint(20,60)
        disk=50
        netin=random.randint(2,50)
        netout=random.randint(3,30)
        
    else:
        vcpu=0
        mem=0
        disk=0
        netin=0
        netout=0
    context={
                 "uuid":uuid,
                 "vcpu":vcpu,
                 'mem':mem,
                 'disk':disk,
                 'netin':netin,
                 'netout':netout,
                 }
    return render_to_response('monitor.xml',context,mimetype='application/xml')
def api(request):
    if request.method=="POST":
        post_data=json.loads(request.raw_post_data)
        l(post_data)
        biztype=post_data.get('biztype',None)
        if biztype=='auth':
            return api_auth(request,post_data)
        elif biztype=='images':
            return images(request,post_data)
        elif biztype=='flavors':
            return flavors(request,post_data)
        elif biztype=='servers':
            return servers(request,post_data)
        else:
            context={
            "result" : 1501,
            "message" : "此服务尚未实现,你必须指定biztype={auth|images|flavors|servers}",
            "data":{"biztype":biztype} 
            }
            return render2json(context)
    #else:
        #if request.GET.get('refresh',None)=='1':
            #markdown.markdownFromFile(settings.SMARTAPI_CONFIG['readme']['mdfile'],settings.SMARTAPI_CONFIG['readme']['htmlfile'])
    return render_to_response('api.html',mimetype='text/html')

def apidoc(request,resource_id=0):
#    l(resource_id)
    resource_id=int(resource_id)
    if resource_id >0:
        res=Resource.objects.get(id=resource_id)
        resources=Resource.objects.filter(service=res.service,enable=True).order_by("id",)
        methods=res.resource_method.all().order_by("method")
        errors=res.resource_error.all()
    else:
        resources=Resource.objects.filter(enable=True).order_by("id",)
        methods=None
        res=None
        errors=None
    return render_to_response('apidoc.html',RequestContext(request, {'resources':resources,'res':res,'methods':methods,'errors':errors}))
    pass
def api_auth(request,post_data):
    if haskeys(post_data['bizdata'],'username','password'):
        context=getToken(post_data['bizdata']['username'],post_data['bizdata']['password'],post_data['tenantid'])
    else:
        context={
                 "result" : 1400, # 0,
                "message" : "数据格式非法,POST的数据至少包含username,password,tenantid三个字段", #返回值描述, 上面code的文字描述
                "data" : post_data
                 }
    return render2json(context)
def images(request,post_data):
    context=getImageList(post_data["token"])
    return render2json(context)
def flavors(request,post_data):
    if haskeys(post_data,'token','tenantid'):
        context=getFlavorList(post_data["token"],post_data["tenantid"])
    else:
        context={
            "result" : 1400, # 0,
            "message" : "数据格式非法，请使用POST提交数据,并且至少包含token,tenantid两个字段", 
          }
    return render2json(context)
def servers(request,post_data):
    action=post_data.get('action',None)
    if action=='create':
        if haskeys(post_data['bizdata'],'imageRef','flavorRef','name'):
            context=createServer(post_data['token'],post_data['tenantid'],post_data['bizdata']['imageRef'],post_data['bizdata']['flavorRef'],post_data['bizdata']['name'])
        else:
            context={
                "result" : 1400, 
                "message" : "bizdata必须包含imageRef,flavorRef,name", 
              }
    elif action=='retrieve':
        context=getServerList(post_data['token'],post_data['tenantid'])
    elif action=='delete':
        context=deleteServer(post_data['token'],post_data['tenantid'],post_data['bizdata']['serverid'])
    else:
        context={
                 "result":1503,
                 "message":"action未实现",
                 }
    
    return render2json(context)

def proxy(request):
    '''     
    proxy_var={
           "path":request.path,
           "get":request.GET,
           'post':request.POST,
           'host':request.get_host(),
           'headers':headers,
           'body':request.body,
           'method':request.method,
           'query_string':request.META['QUERY_STRING'],
           } 
    error: {
body: "",
headers: {
Content-Type: "application/json"
},
host: "192.168.1.1",
code: 504,
title: "API Gateway unreachable",
url: "/v1/images",
message: "",
port: 9292,
method: "GET"
}
           '''
    #l(request)
    #/smartapi/api/image/images
    service_code=request.path.split('/')[2]
    l("service:"+service_code)
    if service_code == "":
        return apidoc(request,0)
#        return render_to_response('api.html',mimetype='text/html')
    try:
        service=Service.objects.get(code=service_code)
        url = request.path.replace('api/'+service.code,service.prefix,1)
        if len(request.META['QUERY_STRING'])>0:
            url='%s?%s' % (url,request.META['QUERY_STRING'])
        headers = {"Content-Type": "application/json"}
        if 'HTTP_X_AUTH_TOKEN' in request.META.keys():
            headers['X-Auth-Token']=request.META['HTTP_X_AUTH_TOKEN']
            headers['Content-Type']=request.META['CONTENT_TYPE']
        r = restclient(service.host, service.port, url, request.method, request.body, headers)
        return render2json(r)
    except Exception,e:
        error={'error':{
               "code":400,
               "message":e.message,
               }}
        return render2json(error)
        
    
    
    

def auth(request):
    pass
def compute(request):
    pass
def image(request):
    pass
def volume(request):
    pass
if __name__ == '__main__':
    '''test'''
    a=os.path.abspath(__file__)
    print a