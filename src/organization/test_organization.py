# -*- coding: utf-8 -*-
'''
Created on 2018年4月19日

@author: Simba
'''


import unittest
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON
import config.config as CONFIG


class OrgTestCase(unittest.TestCase):

    # 参数
    # 获取查询参数
    parameterListForAddOrg = {
        "OrgName":"add org test",
        "OrgLevel":  1,
        "SuperiorOrgId":"0000",
        "Comment":"just for test"
    }
    
    # 修改组织所需参数
    parameterListForUpdateOrg = {
        "OrgName":"update org test originalaaa.",
        "OrgLevel":  1,
        "SuperiorOrgId":"0000",
        "Comment":"just for test"
    }
    
    # 获取查询组织列表接口的参数
    paramListForGetOrgs = COMMON.getParametersFromFiles("get_organizations.parameters")
    
    # add org test
    def test_addOrg(self):
        
        # 增加组织
        addUrl = "http://%s:%s/api/orgs" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        addOrgSource = self.parameterListForAddOrg
        resAddObject = HTTP_REQUEST.post_request(addUrl, addOrgSource)
        orgIdStr = resAddObject[0]["OrgId"]
        
        # 获得上级组织的名称
        getSuperOrgNameUrl = "http://%s:%s/api/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, addOrgSource["SuperiorOrgId"])
        resGetSuperOrgNameObject = HTTP_REQUEST.get_request(getSuperOrgNameUrl)
        
        # 验证
        self.assertEqual(200, resAddObject[1])
        self.assertEqual(unicode(self.parameterListForAddOrg["Comment"], "utf-8"), resAddObject[0]["Comment"])
        self.assertEqual(unicode(self.parameterListForAddOrg["OrgName"], "utf-8"), resAddObject[0]["OrgName"])
        self.assertEqual(unicode(self.parameterListForAddOrg["SuperiorOrgId"], "utf-8"), resAddObject[0]["SuperiorOrgId"])
        self.assertEqual(self.parameterListForAddOrg["OrgLevel"], resAddObject[0]["OrgLevel"])
        self.assertEqual(resGetSuperOrgNameObject[0]["SuperiorOrgName"], resAddObject[0]["SuperiorOrgName"])
        
        # 删除组织（复原）
        delUrl = "http://%s:%s/api/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, orgIdStr)
        resDelObject = HTTP_REQUEST.del_request(delUrl)
        
        self.assertEqual(200, resDelObject[1])
    
    
    # 删除
    # 增加组织中已验证
    
    # 修改
    def test_updateOrg(self):
        """
        1. 增加组织
        2. 修改组织名称
        3. 删除组织
        """
        updateOrgSource = self.parameterListForUpdateOrg
        addOrgUrl = "http://%s:%s/api/orgs" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        
        resAddOrgObject = HTTP_REQUEST.post_request(addOrgUrl, updateOrgSource)
        orgIdStr = resAddOrgObject[0]["OrgId"]
         
        updateOrgUrl = "http://%s:%s/api/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, orgIdStr)
        updateOrgSource = resAddOrgObject[0]
        updateOrgSource["OrgName"] = "update org test updated."
         
        resUpdateOrgObject = HTTP_REQUEST.put_request(updateOrgUrl, updateOrgSource)
         
        self.assertEqual(200, resUpdateOrgObject[1])
        self.assertEqual("update org test updated.", resUpdateOrgObject[0]["OrgName"])
         
        delUrl = "http://%s:%s/api/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, orgIdStr)
        resDelObject = HTTP_REQUEST.del_request(delUrl)
         
        self.assertEqual(200, resDelObject[1])
    
    # 通过组织ID查询组织
    # 增加组织中已验证（查询上级组织）
    
    
    # 查询组织信息列表
    def test_getOrgss(self):

            for i in self.paramListForGetOrgs:
                offsetStr, limitStr = i
                url = "http://%s:%s/api/orgs?offset=%s&limit=%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, offsetStr, limitStr)
    
                resObject = HTTP_REQUEST.get_request(url)
    
                # 接口调用成功，验证返回码
                self.assertEqual(200, resObject[1])
                
                # print len(resObject[0]["list"])
                
                # 验证返回结果
                if limitStr == "*":
                    pass
                else:
                    self.assertTrue(len(resObject[0]["list"]) <= int(limitStr))
        


if __name__ == '__main__':
    unittest.main()
