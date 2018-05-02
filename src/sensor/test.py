# -*- coding: utf-8 -*-
'''
Created on 2018年4月19日

@author: Simba
'''


import unittest
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON
import config.config as CONFIG
import time



class SensorTestCase(unittest.TestCase):
    
    def getSensorID(self):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    paramListForAddCloudSensor = {
        "OrgId":"496ec20d-1855-4ff4-9c9d-993aaf7d6d20",
        "SensorId":"2018041901",
        "SensorName":"forAddCloudSensor"}
    
    
    
#     # 按设备id查询设备
#     # 2018041902
#     def test_getSensorById(self):
#         
#         sensorIdStr = "2018041902"
#         url = "http://%s:%s/api/sources/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, sensorIdStr)
#         
#         resObject = HTTP_REQUEST.get_request(url)
#         
#         # 验证返回码
#         self.assertEqual(200, resObject[1])
        
        
#         delSensorUrl = "http://%s:%s/api/sources/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, "2018041902")
#         resDelSensorObject = HTTP_REQUEST.del_request(delSensorUrl)
#         self.assertEqual(200, resDelSensorObject[1])
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        