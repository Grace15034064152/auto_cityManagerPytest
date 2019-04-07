import pytest
import allure
from conftest import http
from common.commonData import CommonData
@allure.feature("修改密码模块")
class Test_ChangePwd:
    @allure.story("修改密码成功")

    def test_changePwd_success(self):
        path = "/sys/changePwd"
        data = {
                'userId':114,
                'userName': CommonData.mobile,
                'oldPwd': CommonData.password,
                'password':'147258'
                }
        resp = http.post(path,data)
        print(resp)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
    @allure.story("恢复密码成功")
    def test_changePwd_recovery(self):
        # httputil = HttpUtil()
        path = "/sys/changePwd"
        data = {
            'userId': 114,
            'userName': CommonData.mobile,
            'oldPwd': '147258',
            'password': CommonData.password
        }
        resp = http.post(path, data)
        print(resp)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
