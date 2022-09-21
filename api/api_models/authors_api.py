from final_project.api.api_models.base_api import BaseApi


class AuthorsApi(BaseApi):
    def __init__(self, url=None, headers=None):
        super().__init__(url, headers)
        self._url = f'{self._url}Authors'

    def get_authors(self):
        res = self.session.get(url=f"{self._url}")
        return res

    def post_authors(self, author):
        res = self.session.post(url=f"{self._url}", json=author.to_json())
        return res

    def get_author_id(self, id:int):
        res = self.session.get(url=f"{self._url}/{id}")
        return res

    def put_author_byid(self, id:int, updateauthor):
        res = self.session.put(url=f"{self._url}/{id}",json=updateauthor.to_json())
        return res

    def delete_authors_id(self, authorsid):
        res = self.session.delete(url=f"{self._url}/{authorsid}")
        return res

    def get_authors_search_txt(self, txt:str):
        res = self.session.get(url=f"{self._url}/search/{txt}")
        return res
