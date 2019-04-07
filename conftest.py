import pytest
from util.httputil import HttpUtil
from common.commonData import CommonData

#module/session/class/function
http = HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def fixture():
    path="/sys/login"
    data={'userName': CommonData.mobile,'password': CommonData.password}
    res_login=http.post(path,data)
    CommonData.token=res_login['object']['token']
    print(res_login['object']['token'])
    print(res_login)
    assert res_login['code']==200
    print("登录成功")

    yield #退出当前函数
    path="/sys/logout"
    data=None
    res_logout = http.post(path,data)
    print(res_logout)
    # assert  res_logout['code']==200
    print("退出登录")
