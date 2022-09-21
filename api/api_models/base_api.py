import requests


class BaseApi:
    def __init__(self, url: str, headers: None):
        self._url = f"{url}:7017/api/"
        if headers:
            self._headers = headers
        else:
            self._headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self._headers)

