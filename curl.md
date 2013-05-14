curl -d '{"auth":{"passwordCredentials": {"username": "admin", "password": "password"}}}' -H "Content-type: application/json" http://127.0.0.1:5000/v2.0/tokens

curl -v -H "X-Auth-Token:dba0a6722b86483e83b07e5556bafb02" http://192.168.1.1:9292/v1/images 


curl -k -X 'POST' -v http://192.168.1.1:5000/v2.0/tokens -d '{"auth":{"passwordCredentials":{"username": "admin", "password":"password"}, "tenantId":"3942bfc544a24f748788c06dbc486ffa"}}' -H 'Content-type: application/json'

dba0a6722b86483e83b07e5556bafb02

curl -v -H "X-Auth-Token:dba0a6722b86483e83b07e5556bafb02" http://192.168.1.1:8774/v2/3942bfc544a24f748788c06dbc486ffa/servers


