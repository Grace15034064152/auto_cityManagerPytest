from conftest import http
from common.commonData import CommonData
import allure
@allure.feature("获取用户信息")
class Test_userInfo():
    @allure.story("获取用户信息成功")
    #     @pytest.mark.usefixtures("getuserInfo")
    def test_userInfo(self):
        print("得到用户信息")
        path="/sys/getUserInfo"
        headers=http.headers
        headers["token"]=CommonData.token
        data=None
        resq=http.post(path,data)
        print(resq)