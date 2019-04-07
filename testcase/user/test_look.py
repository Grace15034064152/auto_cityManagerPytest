import pytest
import random
from conftest import http
from common.commonData import CommonData
import allure
@allure.feature("注册模块")
class Test_Look:
    @allure.story("注册成功")

    def test_look_success(self):
        #注册
        print("注册")
        nickname=str(random.randint(10000000,10000000))
        mobile='139'+nickname
        path = "/user/saveOrUpdateUser"
        data = {
                'nickName':nickname ,
	            'userName':mobile ,
	            'telNo': '',
	            'email': '',
	            'address': '',
	            'roleIds': '',
	            'regionId': 1,
	            'regionLevel': 1
                }
        resp = http.post(path,data)
        print(resp)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        #登录
        print("登录")
        path = "/sys/login"
        name=data['userName']
        data = {'userName': name, 'password': CommonData.password}
        resp = http.post(path,data)
        print(resp)
        assert resp['code']==200
        id=resp['object']['userId']
        print(id)
        #查看列表
        print("查看列表")
        path = "/user/loadUserList"
        data = {"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}
        resp = http.post(path, data)
        print(resp)
        assert resp['code'] == 200
        assert resp['object']['list'][0]['id']==id
        #获取用户详情
        print("获取用户详情")
        path = "/user/loadUserInfo"
        data = {'id':id}
        resp = http.post(path, data)
        print(resp)
        assert resp['code'] == 200

#