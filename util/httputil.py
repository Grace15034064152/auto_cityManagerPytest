import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http=requests.session() #作用于全局加self
        self.headers= {'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data=None):
        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)

        if CommonData.token is not None:
            self.headers['token']=CommonData.token
        res_login = self.http.post(url=host+path,
                             proxies=proxies,
                             data=data_json,
                             headers=self.headers)
        assert res_login.status_code==200
        res_json=res_login.text
        res_dict=json.loads(res_json)
        return res_dict




