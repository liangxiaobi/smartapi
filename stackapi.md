#Openstack API 开发备注

##http://api.openstack.org/api-ref.html

#Keystone v2.0

##Request POST v2.0/tokens
    {
        "auth":{
            "passwordCredentials":{
                "username":"admin",
                "password":"passworD!"
            },
            "tenantId":"bb49f6cec9c748c1a57ffb147191c911"
        }
    }

##Response
####Normal
    {
      "access" : {
        "token" : {
          "expires" : "2013-01-22T05:47:55Z",
          "id" : "9c4725b11d1440738ee9a1e9703175d3",
          "tenant" : {
            "description" : null,
            "enabled" : true,
            "id" : "60bb1d7ea05b4d0aaffb90352cd6576c",
            "name" : "admin"
          }
        },
        "serviceCatalog" : [ {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c",
            "publicURL" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c"
          } ],
          "endpoints_links" : [],
          "type" : "compute",
          "name" : "nova"
        }, {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:9292/v1",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:9292/v1",
            "publicURL" : "http://192.168.10.2:9292/v1"
          } ],
          "endpoints_links" : [ ],
          "type" : "image",
          "name" : "glance"
        }, {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:8776/v1/60bb1d7ea05b4d0aaffb90352cd6576c",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:8776/v1/60bb1d7ea05b4d0aaffb90352cd6576c",
            "publicURL" : "http://192.168.10.2:8776/v1/60bb1d7ea05b4d0aaffb90352cd6576c"
          } ],
          "endpoints_links" : [ ],
          "type" : "volume",
          "name" : "volume"
        }, {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:8773/services/Admin",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:8773/services/Cloud",
            "publicURL" : "http://192.168.10.2:8773/services/Cloud"
          } ],
          "endpoints_links" : [ ],
          "type" : "ec2",
          "name" : "ec2"
        }, {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:8080/v1",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:8080/v1/AUTH_60bb1d7ea05b4d0aaffb90352cd6576c",
            "publicURL" : "http://192.168.10.2:8080/v1/AUTH_60bb1d7ea05b4d0aaffb90352cd6576c"
          } ],
          "endpoints_links" : [ ],
          "type" : "object-store",
          "name" : "swift"
        }, {
          "endpoints" : [ {
            "adminURL" : "http://192.168.10.2:35357/v2.0",
            "region" : "RegionOne",
            "internalURL" : "http://192.168.10.2:5000/v2.0",
            "publicURL" : "http://192.168.10.2:5000/v2.0"
          } ],
          "endpoints_links" : [ ],
          "type" : "identity",
          "name" : "keystone"
        } ],
        "user" : {
          "username" : "admin",
          "roles_links" : [ ],
          "id" : "cd5bde66bd5e48e0bb4f861fe77a23b3",
          "roles" : [ {
            "id" : "41708d5a9b5045449eda8df919a5fcd3",
            "name" : "KeystoneAdmin"
          }, {
            "id" : "7e09f42e3272403696c4b30a749e733c",
            "name" : "KeystoneServiceAdmin"
          }, {
            "id" : "c4548bed57384b7ebebe5884d6aead4a",
            "name" : "admin"
          } ],
          "name" : "admin"
        }
      }
    }

####Error
    {
      "error" : {
        "message" : "Invalid user / password","InInvalid tenant",
        "code" : 401,
        "title" : "Not Authorized"
      }
    }

#IMAGES V1.1
http://docs.openstack.org/api/openstack-image-service/1.1/content/
##LIST
###Request 
GET 9292/v1/images?name=&container_format=&disk_format=&satus=&size_min=&size_max=

###Response
{
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

#Flavor V2.0
##LIST 
###Request 
GET 8774/v2/{tenantid}/flavors?miniDisk=%s&miniRam=%s

### Response
{
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

#Server v2.0#

##LIST
GET http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/servers?image=imageRef&tenant_id=11&flavor=flavorRef&name=serverName&status=serverStatus&marker=markerID&limit=11&changes-since=1358844619.7 
###Response
"servers" : [ {
          "OS-EXT-STS:task_state" : null,
          "addresses" : {
            "private" : [ {
              "version" : 4,
              "addr" : "192.0.0.8"
            } ]
          },
          "links" : [ {
            "href" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/servers/10c1050e-50cf-4ad8-850a-c12f3d9b9409",
            "rel" : "self"
          }, {
            "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/servers/10c1050e-50cf-4ad8-850a-c12f3d9b9409",
            "rel" : "bookmark"
          } ],
          "image" : {
            "id" : "e40adcfe-5226-44e1-a97b-d57f17dcf93e",
            "links" : [ {
              "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/images/e40adcfe-5226-44e1-a97b-d57f17dcf93e",
              "rel" : "bookmark"
            } ]
          },
          "OS-EXT-STS:vm_state" : "active",
          "OS-EXT-SRV-ATTR:instance_name" : "instance-00000018",
          "flavor" : {
            "id" : "2",
            "links" : [ {
              "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/2",
              "rel" : "bookmark"
            } ]
          },
          "id" : "10c1050e-50cf-4ad8-850a-c12f3d9b9409",
          "user_id" : "cd5bde66bd5e48e0bb4f861fe77a23b3",
          "OS-DCF:diskConfig" : "MANUAL",
          "accessIPv4" : "",
          "accessIPv6" : "",
          "progress" : 0,
          "OS-EXT-STS:power_state" : 1,
          "config_drive" : "",
          "status" : "ACTIVE",
          "updated" : "2013-01-22T08:24:20Z",
          "hostId" : "4f6133690cc2d6a695ea40c7b114b811a3da2dc52a51cfe872ceb1d3",
          "OS-EXT-SRV-ATTR:host" : "sns",
          "key_name" : "",
          "OS-EXT-SRV-ATTR:hypervisor_hostname" : null,
          "name" : "new-server-test",
          "created" : "2013-01-22T08:23:59Z",
          "tenant_id" : "60bb1d7ea05b4d0aaffb90352cd6576c",
          "metadata" : {
            "My Server Name" : "Server1"
          }
        }, {
          "OS-EXT-STS:task_state" : null,
          "addresses" : {
            "private" : [ {
              "version" : 4,
              "addr" : "192.0.0.7"
            } ]
          },
          "links" : [ {
            "href" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/servers/4dea8f30-6531-4bce-a5a9-61023483c61f",
            "rel" : "self"
          }, {
            "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/servers/4dea8f30-6531-4bce-a5a9-61023483c61f",
            "rel" : "bookmark"
          } ],
          "image" : {
            "id" : "e40adcfe-5226-44e1-a97b-d57f17dcf93e",
            "links" : [ {
              "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/images/e40adcfe-5226-44e1-a97b-d57f17dcf93e",
              "rel" : "bookmark"
            } ]
          },
          "OS-EXT-STS:vm_state" : "active",
          "OS-EXT-SRV-ATTR:instance_name" : "instance-00000017",
          "flavor" : {
            "id" : "2",
            "links" : [ {
              "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/flavors/2",
              "rel" : "bookmark"
            } ]
          },
          "id" : "4dea8f30-6531-4bce-a5a9-61023483c61f",
          "user_id" : "cd5bde66bd5e48e0bb4f861fe77a23b3",
          "OS-DCF:diskConfig" : "MANUAL",
          "accessIPv4" : "",
          "accessIPv6" : "",
          "progress" : 0,
          "OS-EXT-STS:power_state" : 1,
          "config_drive" : "",
          "status" : "ACTIVE",
          "updated" : "2013-01-22T08:24:11Z",
          "hostId" : "4f6133690cc2d6a695ea40c7b114b811a3da2dc52a51cfe872ceb1d3",
          "OS-EXT-SRV-ATTR:host" : "sns",
          "key_name" : "",
          "OS-EXT-SRV-ATTR:hypervisor_hostname" : null,
          "name" : "new-server-test",
          "created" : "2013-01-22T08:23:58Z",
          "tenant_id" : "60bb1d7ea05b4d0aaffb90352cd6576c",
          "metadata" : {
            "My Server Name" : "Server1"
          }
        } ]
##Create
POST v2/{tenant_id}/servers
###Request
{
    "server": {
        "flavorRef": "2",
        "imageRef": "e40adcfe-5226-44e1-a97b-d57f17dcf93e",
        "metadata": {
            "My Server Name": "Apache1"
        },
        "name": "new-server-test",
        "personality": []
    }
}
###Response
{
  "server" : {
    "OS-DCF:diskConfig" : "MANUAL",
    "id" : "b995c16d-d6ad-409a-b48b-6a02ef8d03f5",
    "links" : [ {
      "href" : "http://192.168.10.2:8774/v2/60bb1d7ea05b4d0aaffb90352cd6576c/servers/b995c16d-d6ad-409a-b48b-6a02ef8d03f5",
      "rel" : "self"
    }, {
      "href" : "http://192.168.10.2:8774/60bb1d7ea05b4d0aaffb90352cd6576c/servers/b995c16d-d6ad-409a-b48b-6a02ef8d03f5",
      "rel" : "bookmark"
    } ],
    "adminPass" : "GU8xLHDz9Ace"
  }
}

