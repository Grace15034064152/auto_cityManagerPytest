import pytest
from conftest import http
# import allure
# from common.commonData import CommonData
# @allure.feature("登录模块")
# class Test_login:
#     allure.story("登录成功")

#     def test_login_success(self):

        # path = "/sys/login"
        # data = {'userName': CommonData.mobile, 'password': CommonData.password}
        # resp = http.post(path,data)
        # print(resp)
        # assert resp['code']==200
        # assert resp['msg']=='操作成功'
        # assert resp['object']['userId']==2

    # def test_login_fail1(self):
    #     data = {'userName': '111', 'password': CommonData.password}
    #
    #     path = '/sys/login'
    #     resp = http.post(path,data)
    #     assert resp['code'] == 301
    #     assert resp['msg'] == '用户不存在'
    #
    # def test_login_fail2(self):
    #     data = {'userName':CommonData.mobile , 'password': '11111'}
    #
    #     path = '/sys/login'
    #     resp = http.post(path, data)
    #     assert resp['code'] == 410
    #     assert resp['msg'] == '用户名或密码错误'
    #
    # def test_login_fail3(self):
    #     data = {'userName':'' , 'password': '11111'}
    #     path = '/sys/login'
    #     resp = http.post(path, data)
    #     assert resp['code'] == 3010
    #     assert resp['msg'] == '此账户禁止登录'
    #
    #
    #

