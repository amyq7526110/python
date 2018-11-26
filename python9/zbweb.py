import  requests
import  json
url = 'http://192.168.1.70/api_jsonrpc.php'
header = {'Content-Type':'application/json-rpc'}
#https://www.zabbix.com
# data = {
#     "jsonrpc": "2.0",                  # 固定的协议版本
#     "method": "apiinfo.version",       # 方法官方文档上查
#     "params": [],                      # 参数
#     "id": 1                            # 随便一个数字
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
#
# data = {                    # 获取主机信息
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         # "filter": {
#         #     "host": [
#         #         "Zabbix server",
#         #         "Linux server"
#         #     ]
#         # }
#     },
#     "auth": "21731b1f58c5e13ead56f14e4889bf3e",
#     "id": 1
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "21731b1f58c5e13ead56f14e4889bf3e",
#     "id": 1
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         # "13",
#         "10254"
#     ],
#     "auth": "21731b1f58c5e13ead56f14e4889bf3e",
#     "id": 1
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "21731b1f58c5e13ead56f14e4889bf3e",
#     "id": 1
# }
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web_server2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.72",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "52:54:00:d2:2b:c8"
            # "macaddress_b": "56768"
        }
    },
    "auth": "21731b1f58c5e13ead56f14e4889bf3e",
    "id": 1
}

r = requests.post(url,data=json.dumps(data),headers=header)

print(r.json())