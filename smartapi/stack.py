# -*- encoding=utf8 -*-
'''
Created on 2012-12-12
1
@author: lion
'''
from django.conf import settings
from smartapi.novamodel import InstanceTypes
from smartapi.tools import l
import httplib
import inspect
import json
import logging
import time

def restclient(host, port, url, method, body, headers,):
    debug = inspect.stack()[1]
    logging.debug("Restclient:%s %s \n\t URL: http://%s:%s%s \n\t Body: %s \n\t Headers: %s" % (debug[3], method, host, port, url, body, headers))
    try:
        conn = httplib.HTTPConnection("%s:%s" % (host,port))
        conn.request(method, url, body, headers)
        data=conn.getresponse()
        l(data.status)
        if data.status==401:
            error={
              "error" : {
                "message" : "Unauthorized",
                "code" : 401,
                "title" : "Token is invalid.",
                "host":host,
                "port":port,
                "url":url,
                "method":method,
                "headers":headers,
                "body":body,
              }
            }
            l(error)
            return error
        elif data.status==404:
            error={
              "error" : {
                "message" : "Resource Not Found ,or the API is not implemented.",
                "code" : 404,
                "title" : "No items is found.",
                "host":host,
                "port":port,
                "url":url,
                "method":method,
                "headers":headers,
                "body":body,
              }
            }
            return error
        elif data.status==500:
            error={
              "error" : {
                "message" : "Request Failed: internal server error while processing your request.",
                "code" : 500,
                "title" : "Internal server error.",
                "host":host,
                "port":port,
                "url":url,
                "method":method,
                "headers":headers,
                "body":body,
              }
            }
            return error
        elif data.status==204:
            return {"code":204,"message":"No content"}
        elif data.status==202:
            return {"code":202,"message":"Accepted"}
        else:
            return json.loads(data.read())
    except Exception, e:
        l("Error:"+e.message)
#        raise Exception
        error={
              "error" : {
                "message" : e.message,
                "code" : 504,
                "title" : "API Gateway unreachable",
                "host":host,
                "port":port,
                "url":url,
                "method":method,
                "headers":headers,
                "body":body,
              }
            }
        return error
    finally:
        conn.close()
    
def getToken(username, password, tenantid,keystone):
    host=keystone
    #host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '35357'
    url = '/v2.0/tokens'
    method = 'POST'
    body = '{"auth":{"passwordCredentials":{"username": "%s", "password":"%s"}, "tenantId":"%s"}}' % (username, password, tenantid)
    headers = {"Content-Type": "application/json"}
    r = restclient(host, port, url, method, body, headers)
    if r.has_key('access'):
        logging.debug("getToken: %s" % r['access']['token']['id'])
        result=1200
        message="Get token success"
        data={
              "token":r['access']['token']['id'],
               "expire":r['access']['token']['expires'],
               "tenantid":tenantid
            }
    else:
        result=1401
        message="Get token error"
        data = None   
    return data
def getTenantID(keystone_ip, token):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '5000'
    url = 'v2.0/tenants'
    method = 'GET'
    body = ''
    headers = {"Content-Type": "application/json"}
    r = restclient(host, port, url, method, body, headers)
    if r.status == 200:
        data = r.read()
        dd = json.loads(data)
        logging.debug("getTenantID: %s" % dd)
        return dd["tenants"][0]["id"]
    else:
        print "Get Token Error: %s" % r.status
        return False

def getImageList(token):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '9292'
    url = '/v1/images'
    method = 'GET'
    body = None
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.has_key('images'):
        result=1200
        message="Get image list success."
        data = r
    else:
        result=1401
        message="Get image list error."
        data = r
    context={
        "result" :result,
        "message" : message,
        "data" :data
      }
    return context
    
def getFlavorList(token,tenantid, minDisk=0, minRam=0):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '8774'
    url = "/v2/%s/flavors?miniDisk=%s&miniRam=%s" % (tenantid, minDisk, minRam)
    method = 'GET'
    body = None
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.has_key('flavors'):
        result=1200
        message="Get flavor list success."
        data = r
    else:
        result=1401
        message="Get flavor list error."
        data = r
    context={
        "result" :result,
        "message" : message,
        "data" :data
      }
    return context
def getServerList(token,tenantid):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '8774'
    url = "/v2/%s/servers/detail" % (tenantid)
    method = 'GET'
    body = None
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.has_key('servers'):
        result=1200
        message="Get Server list success."
        servers=[]
        ss=r['servers']
        for item in ss:
            servers.append({
                  "addresses" :item['addresses']['private'][0]['addr'],
                  "accessIPv4":item["accessIPv4"],
                  "imageid" : item['image']['id'],
                  "vm_state" : item["OS-EXT-STS:vm_state"],
                  "instance_name" : item["OS-EXT-SRV-ATTR:instance_name"],
                  "flavorid" : item["flavor"]["id"],
                  "id" : item["id"],
                  "user_id" : item["user_id"],
                  "power_state" :item["OS-EXT-STS:power_state"],
                  "status" : item["status"],
                  "updated" : item["updated"],
                  "hostId" : item["hostId"],
                  "host" : item["OS-EXT-SRV-ATTR:host"],
                  "name" : item["name"],
                  "created" : item["created"],
                  "tenant_id" : item["tenant_id"]
                            })
        data = {
          "servers":servers
        }
    else:
        result=1401
        message="Get Server list error."
        data = r
    context={
        "result" :result,
        "message" : message,
        "data" :data
      }
    return context

def createServer(token,tenantid,imageRef,flavorRef,name='newserver'):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '8774'
    url = "/v2/" + tenantid + "/servers"
    method = 'POST'
    body = '{"server" : {"name" :"%s", "imageRef" : "%s",  "flavorRef" : "%s", "metadata" : { "My Server Name" : "Server1" }, "personality" : []     }}' % (name, imageRef, flavorRef)
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.has_key('server'):
        result=1200
        message="Create server success."
        data = r
    else:
        result=1401
        message="Create server  error."
        data = r
    context={
        "result" :result,
        "message" : message,
        "data" :data
      }
    return context

def createFlavor(token, compute_ip, tenantid, vcpus, ram, disk, name=None):
    host = compute_ip
    port = '8774'
    url = "/v2/" + tenantid + "/flavors"
    method = 'POST'
    flavor = InstanceTypes.objects.latest('id')
    flavor_id = flavor.id + 1
    if(name == None):
        name = str(vcpus) + "VCPU-" + str(ram) + "MB_RAM-" + str(disk) + "GB_DISK"
    body = '''{"flavor": {
        "id": "%s",
        "name": "%s",
        "vcpus": %s,
        "ram": %s,
        "disk": %s,
        "OS-FLV-EXT-DATA:ephemeral": 0,
        "rxtx_factor": 2.0,
        "swap": 0
    }}''' % (flavor_id, name, vcpus, ram, disk)
#    logging.debug("Create Flavor URL:http://%s:%s%s" % (host,port,url))
#    logging.debug("Create Flavor Body:%s" % body)
#    
#    logging.debug("Create Flavor Token:%s" % token)
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.status == 200 or r.status == 202:
        data = r.read()
        d = json.loads(data)
        return d['flavor']
    elif r.status == 409:
        
        json_flavor_list = getFlavorList(token, compute_ip, tenantid, disk, ram)
        logging.debug("Flavor exist: %s" % json_flavor_list)
        return json_flavor_list[0]
    else:
        print "Create Flavor Error: %s" % r.status
        return False
def stackclient(work='createserver', name=None, vcpu=None, ram=None, disk=None, serverid=None, systemId=None):
    '''
    work=createserver,deleterserver
    keystone_ip:123.150.200.166
    method:POST,GET,HEAD
    headers:{"Content-Type": "application/json"}
    endpoint:keystone,compute,image,
    params='{"auth":{"passwordCredentials":{"username": "%s", "password":"%s"}, "tenantId":"%s"}}' % (osuser,ospassword,tenantId)
    '''
    
    keystone_ip = settings.OPENSTACK_CONFIG['keystone_ip']
    username = settings.OPENSTACK_CONFIG['username']
    password = settings.OPENSTACK_CONFIG['password']
    tenantid = settings.OPENSTACK_CONFIG['tenantid']
    
    json_token = getToken(username, password, keystone_ip, tenantid)
    token = json_token['token']['id']
    logging.debug("Get %s Token : %s" % (keystone_ip, token))
    if(work == "createserver"):
#        json_image_list=getImageList(token,keystone_ip)
#        print json_image_list
#        imageRef=json_image_list[0]['id']
        logging.debug("System ID is: %s" % systemId);
        if int(systemId) == 1:
            imageRef = 'fdc1f055-b405-48d2-bc67-723527b0cd72'
        else:
            imageRef = 'e40adcfe-5226-44e1-a97b-d57f17dcf93e'
        if None in(vcpu, ram, disk):
            json_flavor_list = getFlavorList(token, keystone_ip, tenantid)
            print json_flavor_list
            flavorRef = json_flavor_list[0]['id']
        else:
            json_flavor = createFlavor(token, keystone_ip, tenantid, vcpu, ram, disk)
            if json_flavor:
                flavorRef = json_flavor['id']
            else:
                json_server = {'id':'0', 'error':'500', 'errormsg':'Create Flavor Error.'}
                return json_server
        print flavorRef
        print imageRef
        if name == None:
            name = "myserver" + str(time.time())
        json_server = createServer(token, keystone_ip, flavorRef, imageRef, tenantid, name)
        return json_server
    if(work == 'createflavor'):
        json_flavor = createFlavor(token, keystone_ip, tenantid, '1024', '2', '10')
        return json_flavor
    if(work == 'deleteserver'):
        delete_server = deleteServer(token, keystone_ip, tenantid, serverid)
        return delete_server
def deleteServer(token,tenantid, serverid):
    host = settings.OPENSTACK_CONFIG['keystone_ip']
    port = '8774'
    url = "/v2/%s/servers/%s" % (tenantid, serverid)
    method = 'DELETE'
    body = ""
    headers = {"Content-Type": "application/json", "X-Auth-Token":token}
    r = restclient(host, port, url, method, body, headers)
    if r.get('code',None)==204:
        result=1204
        message="Sever is deleted."
        data = r
    else:
        result=1404
        message="Server Not Found."
        data = r
    context={
        "result" :result,
        "message" : message,
        "data" :data
      }
    return context
def test(aa='bb'):
    print aa
def getAPIHost(path):
    pass
if __name__ == '__main__':
#    server=stackclient(work='createserver')
#    print server
#    print server['id']
#    return=stackclient(work='createserver',name='myservername',vcpu=1,ram=128,disk=0)
#    re=stackclient(work='createserver',name='myservername',vcpu=1,ram=128,disk=0)
    re = stackclient(work='deleteserver', serverid='')
    print re
