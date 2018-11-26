#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import requests
import sys
def send_msg(url,remiders,msg):
    header = {'Content-Type':'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": remiders,
	    "isAtAll": False,	
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=header)
    return r.text
if __name__ == '__main__':
    msg = sys.argv[1]
    remiders = []
    url = 'https://oapi.dingtalk.com/robot/send?access_token=92dff31a64c67f444173016abf71311543e9c28fe14439dfc630955653c3a3c8'
    print send_msg(url, remiders, msg)
