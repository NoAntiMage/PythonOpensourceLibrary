import requests
import json
from hashlib import md5
import traceback
import datetime


class Zentao(object):
    def __init__(self, host, account, password):
        self.host = host
        self.session_id = ""
        self.params = {}
        self.account = account
        self.password = password

    def get_session_id(self):
        try:
            api_path = "/api-getSessionID.json"
            response = requests.get(self.host + api_path)
            ret = response.json()
#            print(ret)
            data, err = self._valid_zentao_result(ret)
            if err is not None:
                print(err)
            self.session_id = data.get("sessionID")
            sessionName = data.get("sessionName")
            if sessionName is not None:
                self.params[sessionName] = self.session_id
#            print(self.params)
        except Exception:
            traceback.print_exc()

    def login(self):
        try:
            api_path = "/user-login.json"
            login_data = {
                "account": self.account,
                'password': self.password,
            }
            ret = requests.post(self.host + api_path, data=login_data, params=self.params).json()
            if ret['status'] == 'success':
                print("login success")
            else:
                print("login fail")
        except Exception:
            traceback.print_exc()

    def create_user(self, account, password, realname, email):
        try:
            api_path = "/user-create-0.json"
            create_data = {
                "account": account,
                "dept": 0,
                "password1": password,
                "password2": password,
                "realname": realname,
                "join": str(datetime.date.today()),
                "role": "dev",
                "group": 2,
                "email": email,
                "gender": "m",
                "verifyPassword": self._md5(self._md5(self.password) + str(self._get_user_create_rand()))
            }

            response = requests.post(self.host + api_path, data = create_data, params=self.params)
            if response.status_code == 200:
                result = response.json()
                return result
            else:
                print(response.text)
                raise Exception("not 200")
        except Exception:
            traceback.print_exc()



    @staticmethod
    def _valid_zentao_result(result):
        if result['status'] == 'success' and md5(result['data'].encode()).hexdigest() == result['md5']:
            data = json.loads(result['data'])
            return data, None
        return None, "error"

    def _get_user_create_rand(self):
        api_path = "/user-create-0.json"
        response = requests.get(self.host + api_path, self.params)
        data = json.loads((response.json()).get('data'))
        rand = data.get('rand')
        return rand

    def _md5(self, password):
        value = md5(password.encode(encoding='utf8')).hexdigest()
        return value


if __name__ == '__main__':
    zt = Zentao(host="http://localhost:8080",
                account="admin",
                password="123456")

    zt.get_session_id()
    zt.login()
#    rand = zt.get_user_create_rand()
    ret = zt.create_user(account='test',password='test123',realname='测试',email='123@qq.com')
    print(ret)
