# -*- coding: utf-8 -*-
'''
Created on 2018年4月20日

@author: Simba
'''


import unittest
import config.config as CONFIG
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON


class CivilTestCase(unittest.TestCase):
    
    civilAddByRepoIdSource = COMMON.CIVIL
    addRepoSource = {"mode": "white_list", "name": "测试通过repoId添加civil", "type": "person", "capacity": 10006}
    
    # 通过比对库id增加civil
    def test_addCivilByRepoId(self):
        """
            1. 增加比对库，获得比对库ID
            2. 通过比对库ID增加civil
            3. 验证
            4. 删除civil
            5. 删除比对库
        """
        
        # 添加比对库
        addRepoUrl = "http://%s:%s/api/repositories" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        addRepoSource = self.addRepoSource
        
        resAddRepoObject = HTTP_REQUEST.post_request(addRepoUrl, addRepoSource)
        
        repoIdStr = resAddRepoObject[0]["id"]
        print repoIdStr
        
        # 添加civil
        addCivilByRepoIdUrl = "http://%s:%s/api/repositories/%s/entities" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
        civilAddByRepoIdSource = self.civilAddByRepoIdSource
        
        resAddCivilByRepoIdObject = HTTP_REQUEST.post_request(addCivilByRepoIdUrl, civilAddByRepoIdSource)
        print resAddCivilByRepoIdObject
        civilIdStr = resAddCivilByRepoIdObject[0]["id"]
        
        # 验证
        self.assertEqual(201, resAddCivilByRepoIdObject[1])
        
        # 查询
        getCivilByRepoIdAndCivilIdUrl = "http://%s:%s/api/repositories/%s/entities/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr, civilIdStr)
        resGetCivilByRepoIdObject = HTTP_REQUEST.get_request(getCivilByRepoIdAndCivilIdUrl)
        
        self.assertEqual(200, resGetCivilByRepoIdObject[1])
        self.assertEqual(civilAddByRepoIdSource["name"], resGetCivilByRepoIdObject[0]["name"])
        
        # 删除civil
        delCivilByRepoIdAndCivilIdUrl = "http://%s:%s/api/repositories/%s/entities/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr, civilIdStr)
        
        delCivilByRepoIdAndCivilIdObject = HTTP_REQUEST.del_request(delCivilByRepoIdAndCivilIdUrl)
        
        self.assertEqual(200, delCivilByRepoIdAndCivilIdObject[1])
        self.assertEqual(civilAddByRepoIdSource["name"], delCivilByRepoIdAndCivilIdObject[0]["name"])
        self.assertEqual(civilAddByRepoIdSource["id_no"], delCivilByRepoIdAndCivilIdObject["id_no"])
        
        # 再次查询，验证结果为Not Found，表示删除成功
        newResGetCivilByRepoIdObject = getCivilByRepoIdAndCivilIdUrl = "http://%s:%s/api/repositories/%s/entities/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr, civilIdStr)
        
        self.assertEqual(200, newResGetCivilByRepoIdObject[1])
        self.assertEqual("Not Found", newResGetCivilByRepoIdObject[0]["error"])
        
        # 删除比对库
        delRepoUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
        resDelRepoObject = HTTP_REQUEST.del_request(delRepoUrl)
        
        self.assertEqual(200, resDelRepoObject[1])
        
        
if __name__ == '__main__':
    unittest.main()
