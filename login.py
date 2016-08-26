#!/usr/bin/env python
# encoding: utf-8

import base64
import requests
import json


def login(username, password):
    username = base64.b64encode(username.encode('utf-8')).encode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    res = session.post(loginURL, data=postData)
    jsonStr = res.content.decode('gbk')
    info = json.loads(jsonStr)
    if u'0'==info[u'retcode']:
        print '登录成功'
        cookies = session.cookies.get_dict()
        cookies = [key + '=' + value for key, value in cookies.items()]
        cookies = ";".join(cookies)
        session.headers['cookie'] = cookies
    else:
        print '登录失败,原因: %s' %info[u'reason']

if '__main__' == __name__:
    login('你的微博账户名', '你的密码')
