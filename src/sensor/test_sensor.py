# -*- coding: utf-8 -*-
'''
Created on 2018年4月19日

@author: Simba
'''


import unittest
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON
import config.config as CONFIG


class SensorTestCase(unittest.TestCase):
    
    # 参数
    # 获取查询参数
    paramListForGetSensors =  COMMON.getParametersFromFiles("get_sensors.parameters")
    # add cloud sensor
    paramListForAddCloudSensor = {
        "OrgId":"496ec20d-1855-4ff4-9c9d-993aaf7d6d20",
        "SensorId":"2018041901",
        "SensorName":"forAddCloudSensor"}
    # params of search sensor by orgid
    sensorIdForSearchSensorByOrgId = "2018041903"
    # 
    
    
    # add cloud sensor
    def test_addCloudSensor(self):
        """
        验证过程：
        添加设备，验证返回
        """
        addCloudSensorUrl = "http://%s:%s/api/cloudsources" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        addCloudSensorSource = self.paramListForAddCloudSensor
        
        resAddCloudSensor = HTTP_REQUEST.post_request(addCloudSensorUrl, addCloudSensorSource)

        # 验证
        self.assertEqual(201, resAddCloudSensor[1])
        self.assertEqual(1, resAddCloudSensor[0]["status"])
        
        # 通过ID查询设备
        getSensorUrl = "http://%s:%s/api/sources/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, addCloudSensorSource["SensorId"])
        
        resGetSensorByIdObject = HTTP_REQUEST.get_request(getSensorUrl)
        
        # 验证查询返回码
        self.assertEqual(200, resGetSensorByIdObject[1])
        
    
    # 删除设备
    def test_delSensor(self):
        # 通过组织ID查询设备用例中已验证
        pass
    
    
    # 修改设备
    def test_updateSensor(self):
        """
        1. 添加设备
        2. 修改设备
        """
        # 无法修改 "error": "Invalid argument `type`"
        pass
    
        
    # 查询设备
    def test_getSensors(self):

            for i in self.paramListForGetSensors:
                offsetStr, limitStr = i
                url = "http://%s:%s/api/sources?offset=%s&limit=%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, offsetStr, limitStr)
    
                resObject = HTTP_REQUEST.get_request(url)
    
                # 接口调用成功，验证返回码
                self.assertEqual(200, resObject[1])
                
                # print len(resObject[0]["list"])
                
                # 验证返回结果
                if limitStr == "*":
                    pass
                else:
                    self.assertTrue(len(resObject[0]["list"]) <= int(limitStr))
                
    
    # 按设备id查询设备
    # 2018041902
    def test_getSensorById(self):
        
        # 增加设备中已验证
        pass
                    
                   
    # 通过组织ID查询设备
    def test_getSensorByOriId(self):
        
        """
        验证过程：
        1. 添加组织，获得组织ID
        2. 为组织添加设备
        3. 通过组织ID查询设备
        4. 删除设备
        5. 删除组织
        """
        
        addOrgUrl = "http://%s:%s/api/orgs" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        addOrgSource = {
        "OrgName":"add org for test sensor search by org.",
        "OrgLevel":  1,
        "SuperiorOrgId":"0000",
        "Comment":"just for test"
    }
        resAddOrgObject = HTTP_REQUEST.post_request(addOrgUrl, addOrgSource)
        orgIdStr = resAddOrgObject[0]["OrgId"]
        self.assertEqual(201, resAddOrgObject[1])
        
        
        addCloudSensorSource = {
            "OrgId":orgIdStr,
            "SensorId":self.sensorIdForSearchSensorByOrgId,
            "SensorName":self.sensorIdForSearchSensorByOrgId,
    }
        addSensorUrl = "http://%s:%s/api/cloudsources" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        resAddCloudSensor = HTTP_REQUEST.post_request(addSensorUrl, addCloudSensorSource)
        self.assertEqual(201, resAddCloudSensor[1])
        
        getSensorByOrgUrl = "http://%s:%s/api/sources/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, orgIdStr)
        resGetSensorByOrgObject = HTTP_REQUEST.get_request(getSensorByOrgUrl)
        # 验证通过组织查询设备
        self.assertEqual(200, resGetSensorByOrgObject[1])
        self.assertEqual(1, len(resGetSensorByOrgObject[0]["list"]))
        
        # 删除设备
        delSensorUrl = "http://%s:%s/api/sources/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, resAddCloudSensor[0]["SensorId"])
        resDelSensorObject = HTTP_REQUEST.del_request(delSensorUrl)
        self.assertEqual(200, resDelSensorObject[1])
        
        # 删除组织
        delOrgUrl = "http://%s:%s/api/orgs/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, orgIdStr)
        resDelOrgObject = HTTP_REQUEST.del_request(delOrgUrl)
        
        self.assertEqual(200, resDelOrgObject[1])
        
        
        
        
        
        
        
                    
if __name__ == '__main__':
    unittest.main()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    