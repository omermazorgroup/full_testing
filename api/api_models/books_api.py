from final_project.api.api_models.base_api import BaseApi


class BookApi(BaseApi):
    def __init__(self, url=None, headers=None):
        super().__init__(url, headers)
        self._url = f'{self._url}Books'

    def get_books(self):
        res = self.session.get(url=f"{self._url}")
        return res

    def post_book(self, book):
        res = self.session.post(url=f"{self._url}", json=book.to_json())
        return res

    def get_book_byid(self, id:int):
         res = self.session.get(url=f"{self._url}/{id}")
         return res

    def put_book_byid(self, id:int,updatebook):
        res = self.session.put(url=f"{self._url}/{id}", json=updatebook.to_json())
        return res

    def delete_book_byid(self, id:int):
        res = self.session.delete(url=f"{self._url}/{id}")
        return res

    def get_books_by_author_id(self, authorid:int):
        res = self.session.get(url=f"{self._url}/findauthor/{authorid}")
        return res

    def put_book_purchase_byid(self, id:int):
        res = self.session.put(url=f"{self._url}/purchase/{id}")
        return res
