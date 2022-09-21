from final_project.api.api_models.base_api import BaseApi


class AccountApi(BaseApi):
    def __init__(self, url=None, headers=None):
        super().__init__(url, headers)
        self._url = f'{self._url}Account'

    def post_register(self, register):
        res = self.session.post(url=f"{self._url}/register", json=register.to_json())
        return res

    def post_login(self, login):
        res = self.session.post(url=f"{self._url}/login", json=login.to_json())
        return res

    def post_refreshtoken(self, refreshtoken):
        res = self.session.post(url=f"{self._url}/refreshtoken", json=refreshtoken.to_json())
        return res

    def refresh_header(self, header):
        self.session.headers.update(header)
        return self

