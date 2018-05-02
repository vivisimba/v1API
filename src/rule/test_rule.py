# -*- coding: utf-8 -*-
'''
Created on 2018年4月20日

@author: Simba
'''


import unittest
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON
import config.config as CONFIG
import json


class RuleTestCase(unittest.TestCase):
    """
    1. 添加比对库，获得比对库ID
    2. 添加设备，获得设备ID
    3. 添加rule
    4. 查询rule
    5. 删除rule
    6. 删除设备
    7. 删除比对库
    """
    
    def test_addRule(self):
        
        addRuleUrl = "http://%s:%s/api/monitors" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        addRuleSource = {
            "repositories": [
                {
                    "id": "573edd25-8280-49fa-8d34-3ef818afb19c",
                    "threshold": 0.6
                }
            ],
            "source_id": "1427996344",
            "times": {
                "is_persistent": True
            }
        }
        # print addRuleSource
        resAddRuleByIdObject = HTTP_REQUEST.post_request(addRuleUrl, addRuleSource)
        ruleIdStr = resAddRuleByIdObject[0]["id"]
        
        self.assertEqual(201, resAddRuleByIdObject[1])
        
        # 修改
        updateUrl = "http://%s:%s/api/monitors/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, "1427996344")
        updateRuleSource = {
            "repositories": [
                {
                    "id": "573edd25-8280-49fa-8d34-3ef818afb19c",
                    "threshold": 0.7
                }
            ],
            "source_id": "1427996344",
            "times": {
                "is_persistent": True
            }
        }
        resUpdateObject = HTTP_REQUEST.put_request(updateUrl, updateRuleSource)
        self.assertEqual(201, resUpdateObject[1])
        self.assertEqual(0.7, resUpdateObject[0]["repositories"]["threshold"])
        
        # 查询
        queryRuleByIdUrl = "http://%s:%s/api/monitors/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, "1427996344")
        
    # 根据ruleid修改
    def test_updateRuleById(self):
        pass
      
    # 根据ruleid查询
    def test_queryRuleById(self):
        ruleId = "1427996344"
        url = "http://%s:%s/api/monitors/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, ruleId)
        resObject = HTTP_REQUEST.get_request(url)
        
        self.assertEqual(200, resObject[1])
        self.assertEqual(0.7, resObject[0]["repositories"]["threshold"])
        
    # 根据ruleid删除
    def test_delRuleById(self):
        ruleId = "1427996344"
        url = "http://%s:%s/api/monitors/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, ruleId)
        resObject = HTTP_REQUEST.del_request(url)
        
        self.assertEqual(204, resObject[1])
        
    

        
        
        
        
if __name__ == '__main__':
    unittest.main()
