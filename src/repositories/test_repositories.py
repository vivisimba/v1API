# -*- coding: utf-8 -*-
'''
Created on 2018年4月17日

@author: Simba
'''


import unittest
import config.config as CONFIG
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON


class RepositoriesTestCase(unittest.TestCase):

    # 获取查询参数
    paramListForGetRepo = COMMON.getParametersFromFiles("get_repositories.parameters")
    
    # 获取增加比对库接口参数
    paramListForAddRepo = {"mode": "white_list", "name": "曹家渡店#2018-04-18", "type": "person", "capacity": 10006}
    
    # 获取修改比对库接口参数
    # 名称
    paramListForUpdateRepo = {"mode": "white_list", "name": "new曹家渡店#2018-04-18", "type": "person", "capacity": 10006}
    
    # 获取为删除对比库，而新增的对比库信息
    paramListForDelRepo = {"mode": "white_list", "name": "for del repo test.", "type": "person", "capacity": 10006}
    
    # 添加对比库接口
    def test_addRepositories(self):
        '''
        验证过程：添加对比库，验证返回结果，删除新增的对比库
        '''
        url = "http://%s:%s/api/repositories" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        source = self.paramListForAddRepo
        resObject = HTTP_REQUEST.post_request(url, source)
        
        repoIdStr = resObject[0]['id']
        
        # 验证返回码
        self.assertEqual(201, resObject[1])
        # 验证返回结果
        self.assertEqual(self.paramListForAddRepo["mode"], resObject[0]["mode"])
        self.assertEqual(self.paramListForAddRepo["type"], resObject[0]["type"])
        # print self.paramListForAddRepo["name"]
        # print resObject[0]["name"]
        self.assertEqual(unicode(self.paramListForAddRepo["name"], "utf-8"), resObject[0]["name"])
        
        # 删除新增的对比库
        delUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
        HTTP_REQUEST.del_request(delUrl)

    # 删除对比库
    def test_delRepoById(self):
        """
        验证过程：
        1. 调用增加接口，增加新比对库，获取比对库ID
        2. 查询新增比对库，比对库存在
        3. 删除新增比对库，验证返回码
        4. 查询新增比对库，比对库不存在
        """
        # 传入参数准备
        addSource = self.paramListForDelRepo
        
        # 增加比对库
        addUrl = "http://%s:%s/api/repositories" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT)
        resAddObject = HTTP_REQUEST.post_request(addUrl, addSource)
        self.assertEqual(201, resAddObject[1])
        print resAddObject[0]["id"]
        
        # 查询新增比对库
        getUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, resAddObject[0]["id"])
        resGetObject = HTTP_REQUEST.get_request(getUrl)
        self.assertEqual(200, resGetObject[1])
        
        # 删除新增比对库
        delUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, resAddObject[0]["id"])
        resDelObject = HTTP_REQUEST.del_request(delUrl)
        print resDelObject
        
        self.assertEqual(204, resDelObject[1])   #  此处与文档不一致，文档要求返回204，实际返回200
        self.assertEqual(resAddObject[0]["id"], resDelObject[0]["id"])
        self.assertEqual(unicode(self.paramListForDelRepo["type"], "utf-8"), resDelObject[0]["type"])
        self.assertEqual(unicode(self.paramListForDelRepo["name"], "utf-8"), resDelObject[0]["name"])
        self.assertEqual(unicode(self.paramListForDelRepo["mode"], "utf-8"), resDelObject[0]["mode"])
        
        # 再次查询
        resGetObject = HTTP_REQUEST.get_request(getUrl)
        self.assertEqual(404, resGetObject[1])
        
    # 修改对比库
    def test_putRepoById(self):
        '''
            id：唯一标识，应该是不支持修改
            mode：类型，不支持修改
            name：名称，可修改
            type：类别，目前只支持person，所以相当于不可修改
            count：比对库中对象的数量，不通过当前接口修改
            capacity：容量，目前不可修改
            so可修改的只有name
            验证过程：查询指定id的比对库，获得原名称，
                                修改名称
                                再次查询
                                当前名称不等于原名称，当前名称等于修改后名称
                                修改对比库名称为原名称
        '''
         
        repoIdStr = "7d7bc829-e1d4-4d7e-a02e-53e1a2c2e41e"
        newRepoSource = self.paramListForUpdateRepo
        getUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
        updateUrl = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
                
        # 查询原名称
        getRepoByIdResObject = HTTP_REQUEST.get_request(getUrl)
        originalNameStr = getRepoByIdResObject[0]["name"]
        originalRepoSource = {"mode": "white_list", "name": originalNameStr, "type": "person", "capacity": 10006}
        
        # 调用接口修改名称
        updateRepoResObject = HTTP_REQUEST.put_request(updateUrl, newRepoSource)
        # 验证返回码
        self.assertEqual(200, updateRepoResObject[1])
        # 验证名称已修改
        self.assertEqual(unicode(newRepoSource["name"], "utf-8"), updateRepoResObject[0]["name"])
        self.assertNotEqual(originalNameStr, updateRepoResObject[0]["name"])
        
        # 调用修改接口将名称复原
        recoverRepoResObject = HTTP_REQUEST.put_request(updateUrl, originalRepoSource)
        self.assertEqual(200, recoverRepoResObject[1])
        self.assertEqual(originalNameStr, recoverRepoResObject[0]["name"])
        
    # 查询比对库
    def test_getRepositories(self):

            for i in self.paramListForGetRepo:
                offsetStr, limitStr = i
                url = "http://%s:%s/api/repositories?offset=%s&limit=%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, offsetStr, limitStr)
    
                resObject = HTTP_REQUEST.get_request(url)
    
                # 接口调用成功，验证返回码
                self.assertEqual(200, resObject[1])
                
                # print len(resObject[0]["list"])
                
                # 验证返回结果
                if limitStr == "*":
                    pass
                else:
                    self.assertTrue(len(resObject[0]["list"]) <= int(limitStr))
    
    # 通过id查询设备
    # 16435f08-9cb2-4986-891d-09e832b842d0
    def test_getRepoById(self):
        
        repoIdStr = "16435f08-9cb2-4986-891d-09e832b842d0"
        url = "http://%s:%s/api/repositories/%s" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, repoIdStr)
        
        resObject = HTTP_REQUEST.get_request(url)
        
        # 验证返回码
        self.assertEqual(200, resObject[1])
        
    

        


if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
        
        

        
        
        
        