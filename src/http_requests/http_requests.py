# -*- coding: utf-8 -*-
'''
Created on 2018年4月17日

@author: Simba
'''


# import config.config as CONFIG
import requests
import json


# post 增加
def post_request(url, source):
    jsource = json.dumps(source)
    resp = requests.post(url, data = jsource)
    if resp.content == "":
        return None,resp.status_code
    else:
        rdict = json.loads(resp.content)
        return rdict,resp.status_code


# del 删除
def del_request(url):
    resp = requests.delete(url)
    if resp.content == "":
        return None,resp.status_code
    else:
        rdict = json.loads(resp.content)
        return rdict,resp.status_code


# put 修改
def put_request(url, source):
    jsource = json.dumps(source)
    resp = requests.put(url, data = jsource)
    if resp.content == "":
        return None,resp.status_code
    else:  
        rdict = json.loads(resp.content)
        return rdict,resp.status_code
    
    

# get 查询
def get_request(url):
    resp = requests.get(url)
    if resp.content == "":
        return None,resp.status_code
    else:
        rdict = json.loads(resp.content)
        return rdict,resp.status_code
    