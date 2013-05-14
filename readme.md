SmartAPI
=========
本程序为Openstack API 的一个发布，提供友好可读并可测试的ＡＰＩ开发环境

作者：梁肖碧 <11315889@qq.com>

版本 : 1.0


##功能说明:

##镜像：
- 获取镜像列表LIST
- 获取单个镜像信息GET
##主机模板：
- 获取现有模板列表LIST
- 获取单个模板信息GET
- 创建新模板CREATE
- 修改模板MODIFY
- 删除模板DELETE
##主机操作：
- 获取现有主机列表
- 创建新主机
- 修改主机属性
- 删除主机

##主机扩展操作：
- 分配公网IP
- 状态操作:重启、关机、
- VNC查看
- 创建快照

   
##常用工具

###JSON格式化
    <http://www.cnblogs.com/biangbiang/archive/2013/01/11/2856431.html
###Java REST Client
    <http://rest-client.googlecode.com/>
###Groovy RESTCLIENT (groovyx.net.http.RESTClient)    
    <http://groovy.codehaus.org/modules/http-builder/doc/rest.html>
###HttpClient入门
    <http://www.ibm.com/developerworks/cn/opensource/os-httpclient/>
    <http://www.ibm.com/developerworks/cn/aix/library/au-aix-systemsdirector/section2.html>

##接口规范

###通用
- 接口采用http协议访问
- 访问方法有GET、POST、PUT、DELETE四种分别对应查询、创建、修改、删除四种操作
- URL地址: http://hostname:port/api/
- 统一采用POST方式发送数据
- 发送和接收数据采用JSON格式

Request:发送的数据格式,第一层数据均为必填项，无值时使用空字符串""表示

        {
            "token":"string",
            "tenantid":"string",
            "biztype":"{auth|images|flavors|servers|security}",
            "action":"{create|retrieve|update|delete}",
            "bizdata":{
                "param1":"",
                "param2":""
            }
        }
    
- token:认证后获得的令牌
- tenantid:项目id,由管理员指定
- biztype:业务类型{auth|images|flavors|servers|security}
- action:{create|retrieve|update|delete}操作类型
- bizdata:业务数据,参考下面各业务细节  
    
Response:返回的数据格式
    
        {
            "result" : int, # 返回值代码，参见http返回值代码表(由1001-1999,代码后三位为http代码值的参考http代码，其它为自定义代码)
            "message" : "string", #返回值描述, 上面code的文字描述
            "data" : { 
                        "param1":"",
                        "param2":"",
                        ...
                     } #业务数据,参考下面各业务细节
          }

##认证##
首先，登录smartapi的前提是，管理员要分配给你一个用户名、密码、及项目ID
类似这样:
> 用户名:lion
> 密码:password
> 项目ID:aaab5b612c374ce8abbecbb9f20728cc

####说明####
    - 参数 : 
        {
            "token" : "", 
            "tenantid" : "60bb1d7ea05b4d0aaffb90352cd6576c",
            "biztype":"auth",
            "action":"retrieve",
            "bizdata":{
                        "username":"admin", 
                        "password":"password"
                        }
        }
       #biztype=auth时此项可以为空
    - 返回值 :
         {
            "result" : int, # 0,
            "message" : "string", #返回值描述, 上面code的文字描述
            "data" : { 
                        "token":"", #token
                        "expire":"", #过期时间
                     } 
          }
    - 范例 : 

##镜像##
###LIST###
        -Request:
         {
            "token" : "3402c4614e9e457d9ec2daf72337ac31", 
            "tenantid" : "60bb1d7ea05b4d0aaffb90352cd6576c",
            "biztype":"images",
            "action":"retrieve",
            "bizdata":{}
        }
        -Response:
         {
            "result" : int, 
            "message" : "string", 
            "data" : {
                      "images" : [ {
                        "name" : "xxx1",
                        "container_format" : "ovf",
                        "disk_format" : "qcow2",
                        "checksum" : "dd50928018a9d921aa432f97aed8959b",
                        "id" : "59b23f20-15bb-4cfc-bf10-5367ecd59d26",
                        "size" : 2003566592
                      }, {
                        "name" : "ununtu.img",
                        "container_format" : "ovf",
                        "disk_format" : "qcow2",
                        "checksum" : "7bd2c4b925faad477a4258ec98fa7f8e",
                        "id" : "e8356980-bcc9-455d-83dd-c7a82f75963f",
                        "size" : 233832448
                      } ]
                    }
          }
##模板##
获取现有模板列表LIST
 
Request:

    {
        "token" : "3402c4614e9e457d9ec2daf72337ac31", 
        "tenantid" : "60bb1d7ea05b4d0aaffb90352cd6576c",
        "biztype":"flavors",
        "action":"retrieve",
        "bizdata":{}
    }

Response:

    {
        "result" : int, 
        "message" : "string", 
        "data" : {
                  "flavors" : [ {
                    "id" : "1",
                    "links" : [ {
                      "href" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/1",
                      "rel" : "self"
                    }, {
                      "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/1",
                      "rel" : "bookmark"
                    } ],
                    "name" : "m1.tiny"
                  }, {
                    "id" : "2",
                    "links" : [ {
                      "href" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/2",
                      "rel" : "self"
                    }, {
                      "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/2",
                      "rel" : "bookmark"
                    } ],
                    "name" : "m1.small"
                  }]
                }
    }

#主机操作
##创建主机
###Request 
    {
        "token":"3402c4614e9e457d9ec2daf72337ac31",
        "tenantid":"60bb1d7ea05b4d0aaffb90352cd6576c",
        "biztype":"servers",
        "action":"create",
        "bizdata":{
            "flavorRef":"2",
            "imageRef":"e40adcfe-5226-44e1-a97b-d57f17dcf93e",
            "metadata":{
                "My Server Name":"Apache1"
            },
            "name":"new-server-test",
            "personality":[
                
            ]
        }
    }
*name:主机名称
*imageRef:系统镜像id
*flavorRef:模板id
###Response

    {
        "message":"Create server success.",
        "data":{
            "server":{
                "OS-DCF:diskConfig":"MANUAL",
                "id":"3500475d-09e4-43f4-a496-2eb6cb331874",
                "links":[
                    {
                        "href":"http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/servers/3500475d-09e4-43f4-a496-2eb6cb331874",
                        "rel":"self"
                    },
                    {
                        "href":"http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/servers/3500475d-09e4-43f4-a496-2eb6cb331874",
                        "rel":"bookmark"
                    }
                ],
                "adminPass":"dX753xp2qkFi"
            }
        },
        "result":1200
    }
##主机列表
###Request
    {
        "token":"3402c4614e9e457d9ec2daf72337ac31",
        "tenantid":"60bb1d7ea05b4d0aaffb90352cd6576c",
        "biztype":"servers",
        "action":"retrieve"
 }
###Response
    {
  "message" : "Get Server list success.",
  "data" : {
    "servers" : [ {
      "status" : "ACTIVE",
      "vm_state" : "active",
      "updated" : "2013-01-23T02:34:29Z",
      "hostId" : "4f6133690cc2d6a695ea40c7b114b811a3da2dc52a51cfe872ceb1d3",
      "user_id" : "cd5bde66bd5e48e0bb4f861fe77a23b3",
      "addresses" : "192.0.0.2",
      "created" : "2013-01-23T02:34:16Z",
      "tenant_id" : "60bb1d7ea05b4d0aaffb90352cd6576c",
      "imageid" : "e40adcfe-5226-44e1-a97b-d57f17dcf93e",
      "instance_name" : "instance-0000001a",
      "accessIPv4" : "",
      "host" : "sns",
      "power_state" : 1,
      "flavorid" : "2",
      "id" : "77e9036f-0b30-4116-a512-b56223744737",
      "name" : "new-server-test"
    } ]
  },
  "result" : 1200
}
##删除主机
###Request
    {
        "token":"3402c4614e9e457d9ec2daf72337ac31",
        "tenantid":"60bb1d7ea05b4d0aaffb90352cd6576c",
        "biztype":"servers",
        "action":"delete",
        "bizdata":{
            "serverid": "10c1050e-50cf-4ad8-850a-c12f3d9b9409"
        }
    }
###Response
    {
      "message" : "Sever is deleted.",
      "data" : {
        "message" : "No content",
        "code" : 204
      },
      "result" : 1204
    }
    *{
      "message" : "Server Not Found.",
      "data" : {
        "itemNotFound" : {
          "message" : "The resource could not be found.",
          "code" : 404
        }
      },
      "result" : 1404
    }
    
    
#网关版v1.1

这个版本的思路是开发一个网关，主要功能是将来源的API经过一定规则翻译为Opesenstack的API,
用数据库来管理smartapi 与openstack api的对应关系


Request:

