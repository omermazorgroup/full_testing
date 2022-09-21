import unittest
import pytest
import random
import requests
from final_project.api.api_models.account_api import AccountApi
from final_project.api.api_models.authors_api import AuthorsApi
from final_project.api.api_models.books_api import BookApi
from final_project.api.models.loginDto import LoginDto
from final_project.api.models.apiUserDto import ApiUserDto
from final_project.api.models.authResponseDto import AuthResponseDto
from final_project.api.models.authorsDto import AuthorsDto
from final_project.api.models.createBookDto import CreateBookDto
from final_project.api.models.createAuthorDto import CreateAuthorDto
from final_project.api.models.updateAuthorDto import UpdateAuthorDto
from final_project.api.models.bookDto import BookDto
import logging
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture(scope="session")
def url(pytestconfig):
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")


@pytest.fixture(scope="session")
def url(pytestconfig):
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")


@pytest.fixture()
def headers(my_user_register, my_user_login, url):
    """
    A function that set the headers of the request
    :param my_user_register: user details for register
    :param my_user_login: user details for login
    :param url: address of the request
    """
    requests.post(f'{url}:7017/api/Account/register', json=my_user_login.to_json())
    res_login = requests.post(f'{url}:7017/api/Account/login', json=my_user_register.to_json())
    token = res_login.json()["token"]
    headers = {'Authorization': f'Bearer {token}'}
    return headers


@pytest.fixture()
def api_account(headers, url):
    """
    A function that return account's api in the book store
    :param headers: the headers of the request
    :param url: the address of the request
    """
    return AccountApi(url, headers=headers)


@pytest.fixture()
def api_author(headers, url):
    """
    A function that return author's api in the book store
    :param headers: the headers of the request
    :param url: the address of the request
    """
    return AuthorsApi(url, headers=headers)


@pytest.fixture()
def api_book(headers, url):
    """
    A function that return book's api in the book store
    :param headers: the headers of the request
    :param url: the address of the request
    """
    return BookApi(url, headers=headers)


@pytest.fixture()
def new_register() -> ApiUserDto:
    """
    A function that return details for new registration
    """
    email = "a%@gmail.com"
    num = random.randint(0, 1000)
    email = email.replace("%", str(num))
    reg = ApiUserDto(email, "123456", "deborah", "fellous")
    return reg


@pytest.fixture()
def my_user_register() -> ApiUserDto:
    """
    A function that return registration details of my user
    """
    res = ApiUserDto("admin@sela.co.il", "12345", "Omer", "Mazor")
    return res


@pytest.fixture()
def my_user_login() -> LoginDto:
    """
    A function that return login details of my user
    """
    user = LoginDto("admin@sela.co.il", "12345")
    return user


class TestStringMethods(unittest.TestCase):

    def test_post_register(self, new_register, api_account):
        mylogger.info("test for post register")
        # res_post_register = api_account.post_register(new_register)
        # self.assertTrue(res_post_register.status_code == 200)

    # def test_post_register_empty_invalid_email(new_register, api_account):
    #     mylogger.info("test for register with invalid and empty email input")
    #     new_register.email = ""
    #     res_post_register = api_account.post_register(new_register)
    #     assert "The Email field is required." in res_post_register.text
    #     new_register.email = "aaa@"
    #     res_post_register = api_account.post_register(new_register)
    #     assert "The Email field is not a valid e-mail address." in res_post_register.text
    #
    # def test_post_register_invalid_empty_password(new_register, api_account):
    #     mylogger.info("test for register with invalid and empty password input")
    #     new_register.password= "12"
    #     res_post_register = api_account.post_register(new_register)
    #     assert "Your password is limited to 4 to 15 characters" in res_post_register.text
    #     new_register.password = "1234567891234567"
    #     res_post_register = api_account.post_register(new_register)
    #     assert "Your password is limited to 4 to 15 characters" in res_post_register.text
    #     new_register.password = ""
    #     res_post_register = api_account.post_register(new_register)
    #     assert "The Password field is required." in res_post_register.text
    #
    # def test_post_exist_register(my_user_register, api_account):
    #     mylogger.info("test for register with exist user details")
    #     mylogger.info("test for post register")
    #     res_post_register = api_account.post_register(my_user_register)
    #     assert f"Username '{my_user_register.email}' is already taken." in res_post_register.text
    #
    # def test_post_login(my_user_login, api_account):
    #     mylogger.info("test for login with registered user details")
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert userId == res_post_register.json()["userId"]
    #
    # def test_post_login_empty_invalid_email(my_user_login, api_account):
    #     mylogger.info("test for login with empty and invalid email input")
    #     my_user_login.email = ""
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "The Email field is required." in res_post_register.text
    #     my_user_login.email = "aa@"
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "The Email field is not a valid e-mail address." in res_post_register.text
    #
    # def test_post_login_invalid_empty_password(my_user_login, api_account):
    #     mylogger.info("test for login with empty and invalid password input")
    #     my_user_login.password = "1234567"
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "Unauthorized"  in res_post_register.text
    #     my_user_login.password = ""
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "One or more validation errors occurred." in res_post_register.text
    #     my_user_login.password = "123"
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "Your password is limited to 4 to 15 characters" in res_post_register.text
    #     my_user_login.password = "1231231231212313123123"
    #     res_post_register = api_account.post_login(my_user_login)
    #     assert "Your password is limited to 4 to 15 characters" in res_post_register.text
    #
    # def test_post_refreshtoken(api_account, my_user_login):
    #     mylogger.info("test for post refreshtoken")
    #     res_login = api_account.post_login(my_user_login)
    #     my_token = AuthResponseDto(**res_login.json())
    #     res_post_refreshtoken = api_account.post_refreshtoken(my_token)
    #     assert res_post_refreshtoken.json()["userId"] == res_login.json()["userId"]
    #
    # def test_post_refreshtoken_invalid_userId_and_refreshtoken(api_account, my_user_login):
    #     mylogger.info("test for post refrehtoken with invalid userId")
    #     res_login = api_account.post_login(my_user_login)
    #     my_token = AuthResponseDto(**res_login.json())
    #     my_token.userId = "aaaa"
    #     res_post_refreshtoken = api_account.post_refreshtoken(my_token)
    #     assert "Unauthorized" in res_post_refreshtoken.text
    #     my_token = AuthResponseDto(**res_login.json())
    #     my_token.refreshToken = "aaaa"
    #     res_post_refreshtoken = api_account.post_refreshtoken(my_token)
    #     assert "Unauthorized" in res_post_refreshtoken.text
    #
    # @pytest.mark.skip(reason="the response is always 500")
    # def test_post_refreshtoken_invalid_token(api_account, my_user_login, my_user_register): ##500
    #     mylogger.info("test for post refreshtoken with invalid token")
    #     api_account.post_register(my_user_register)
    #     res_login = api_account.post_login(my_user_login)
    #     MyToken = AuthResponseDto(**res_login.json())
    #     MyToken.token = "aaaa"
    #     res_post_refreshtoken = api_account.post_refreshtoken(MyToken)
    #     mylogger.info(res_post_refreshtoken.status_code)
    #     assert "Unauthorized" in res_post_refreshtoken.text
    #
    # def test_get_authors(api_author, new_author):
    #     mylogger.info("test for get all store's authors")
    #     api_author.post_authors(new_author)
    #     res_get_authors = api_author.get_authors()
    #     assert new_author.name in res_get_authors.text
    #
    # def test_post_author(api_author, new_author):
    #     mylogger.info("test for post new author")
    #     res_post_authors = api_author.post_authors(new_author)
    #     assert new_author.name == res_post_authors.json()["name"]
    #
    # def test_post_author_empty_name(api_author, new_author):
    #     mylogger.info("test for post new author with empty name")
    #     new_author.name = ""
    #     res_post_authors = api_author.post_authors(new_author)
    #     assert "The Name field is required." in res_post_authors.text
    #
    # def test_get_author_id(api_author, new_author):
    #     mylogger.info("test for get author by id")
    #     res = api_author.get_authors()
    #     id = res.json()[0]["id"]
    #     res_get_author_byid = api_author.get_author_id(id)
    #     assert id == res_get_author_byid.json()["id"]
    #
    # def test_get_author_invalid_or_not_exist_id(new_author, api_author):
    #     mylogger.info("test get author with invalid and not exist id")
    #     res_get_author_byid = api_author.get_author_id(-1)
    #     assert "Not Found" in res_get_author_byid.text
    #     res_get_authors_id = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors_id)
    #     while True:
    #         num = random.randint(0, len(authors_id)+1)
    #         if num not in authors_id:
    #             res_get_author_byid = api_author.get_author_id(num)
    #             assert "Not Found" in res_get_author_byid.text
    #             break
    #
    # def test_put_author_id(api_author, new_author):
    #     mylogger.info("test for update some author by id")
    #     res = api_author.get_authors()
    #     author_id = res.json()[0]["id"]
    #     update_author = UpdateAuthorDto("UpdateNameAuthor", float(res.json()[0]["homeLatitude"]), float(res.json()[0]["homeLongitude"]), author_id)
    #     res = api_author.put_author_byid(author_id, update_author)
    #     assert res.status_code == 204
    #
    # def test_put_author_id_invalid_id(api_author):
    #     mylogger.info("test for update some author with no exist id")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors)
    #     while True:
    #         num = random.randint(0, len(authors_id) + 1)
    #         if num not in authors_id:
    #             update_author = UpdateAuthorDto("UpdateAuthor", float(res_get_authors.json()[0]["homeLatitude"]),
    #                                                float(res_get_authors.json()[0]["homeLongitude"]), num)
    #             res = api_author.put_author_byid(num, update_author)
    #             assert "Not Found" in res.text
    #             break
    #
    # def test_put_author_id_empty_name(api_author):
    #     mylogger.info("test for update some author with empty name input")
    #     res = api_author.get_authors()
    #     author_id = res.json()[0]["id"]
    #     update_author = UpdateAuthorDto("", float(res.json()[0]["homeLatitude"]), float(res.json()[0]["homeLongitude"]), author_id)
    #     res = api_author.put_author_byid(author_id, update_author)
    #     assert "The Name field is required." in res.text
    #
    # def test_delete_author_byid(api_author):
    #     mylogger.info("test for deleting some author by id")
    #     res = api_author.get_authors()
    #     author_id = res.json()[0]["id"]
    #     res_delete_author = api_author.delete_authors_id(author_id)
    #     assert res_delete_author.status_code == 204
    #     res_get_author_id = api_author.get_author_id(author_id)
    #     assert "Not Found" in res_get_author_id.text
    #
    # def test_delete_author_byid_invalid_id(api_author):
    #     mylogger.info("test for deleting some author with no exist id")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors)
    #     while True:
    #         num = random.randint(0, len(authors_id) + 1)
    #         if num not in authors_id:
    #             res = api_author.delete_authors_id(num)
    #             assert "Not Found" in res.text
    #             break
    #
    # def test_get_author_search(api_author):
    #     mylogger.info("test for searching author by name")
    #     res_get_authors = api_author.get_authors()
    #     authors_name = res_get_authors.json()[0]["name"]
    #     res_get_author_search = api_author.get_authors_search_txt(authors_name)
    #     mylogger.info(res_get_author_search.text)
    #     assert authors_name in res_get_author_search.text
    #
    # def test_get_books(api_book):
    #     mylogger.info("test for get all store's books")
    #     res_get_books = api_book.get_books()
    #     books_name = res_get_books.json()[0]["name"]
    #     mylogger.info(books_name)
    #     assert books_name in res_get_books.text
    #
    # def test_post_book(api_book, api_author):
    #     mylogger.info("test for post new book")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = res_get_authors.json()[0]["id"]
    #     book = new_book(authors_id)
    #     res_post_book = api_book.post_book(book)
    #     assert res_post_book.json()["name"] == book.name
    #
    # def test_post_book_empty_name(api_book, api_author):
    #     mylogger.info("test for post new book with empty name input")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = res_get_authors.json()[0]["id"]
    #     book = new_book(authors_id)
    #     book.name = ""
    #     res_post_book = api_book.post_book(book)
    #     assert "The Name field is required." in res_post_book.text
    #
    # @pytest.mark.skip(reason="the response is allways 500")
    # def test_post_book_invalid_authorid(api_book, api_author):
    #     mylogger.info("test for post new book with no exist author id")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors)
    #     while True:
    #         num = random.randint(0, len(authors_id) + 1)
    #         if num not in authors_id:
    #             book = new_book(num)
    #             res_post_book = api_book.post_book(book)
    #             assert "The authorId field is required." in res_post_book.text
    #             break
    #
    # def test_post_book_error_authorid(api_book):
    #     mylogger.info("test for post new book with invalid author id")
    #     book = new_book(-7)
    #     res_post_book = api_book.post_book(book)
    #     assert "The field AuthorId must be between 1 and 2147483647." in res_post_book.text
    #
    # def test_get_book_byid(api_book):
    #     mylogger.info("test for get some book by id")
    #     res_get_books = api_book.get_books()
    #     book_id = res_get_books.json()[0]["id"]
    #     res_get_book_byid = api_book.get_book_byid(book_id)
    #     assert res_get_books.json()[0]["name"] in res_get_book_byid.text
    #
    # def test_get_book_invalid_byid(api_book):
    #     mylogger.info("test for get some book with no exist id")
    #     res_get_books = api_book.get_books()
    #     books_id = all_books_id(res_get_books)
    #     while True:
    #         num = random.randint(0, len(books_id) + 1)
    #         if num not in books_id:
    #             res = api_book.get_book_byid(num)
    #             assert "Not Found" in res.text
    #             break
    #
    # def test_put_book_byid(api_book, api_author):
    #     mylogger.info("test for update some book by id")
    #     res_get_books = api_book.get_books()
    #     book = BookDto("UpDateNameBook", res_get_books.json()[0]["description"],
    #                                int(res_get_books.json()[0]["price"]), int(res_get_books.json()[0]["amountInStock"]),
    #                                res_get_books.json()[0]["imageUrl"], res_get_books.json()[0]["authorId"],res_get_books.json()[0]["id"])
    #     res_put_book_id = api_book.put_book_byid(res_get_books.json()[0]["id"], book)
    #     assert res_put_book_id.status_code == 204
    #
    # def test_put_book_by_invalid_book_id(api_book, api_author):
    #     mylogger.info("test for update some book with no exist id")
    #     res_get_books = api_book.get_books()
    #     books_id = all_books_id(res_get_books)
    #     while True:
    #         num = random.randint(0, len(books_id) + 1)
    #         if num not in books_id:
    #             book = BookDto(res_get_books.json()[0]["name"], res_get_books.json()[0]["description"],
    #                                int(res_get_books.json()[0]["price"]), int(res_get_books.json()[0]["amountInStock"]),
    #                                res_get_books.json()[0]["imageUrl"], res_get_books.json()[0]["authorId"], num)
    #             res_put_book_id = api_book.put_book_byid(num, book)
    #             assert "Not Found" in res_put_book_id.text
    #             break
    #
    # def test_put_book_byid_empty_name(api_book):
    #     mylogger.info("test for update some book by id with empty name input")
    #     res_get_books = api_book.get_books()
    #     book = BookDto("", res_get_books.json()[0]["description"],
    #                        int(res_get_books.json()[0]["price"]), int(res_get_books.json()[0]["amountInStock"]),
    #                        res_get_books.json()[0]["imageUrl"], res_get_books.json()[0]["authorId"],
    #                        res_get_books.json()[0]["id"])
    #     res_put_book_id = api_book.put_book_byid(res_get_books.json()[0]["id"], book)
    #     assert "The Name field is required." in res_put_book_id.text
    #
    # def test_put_book_by_invalid_authorId(api_book, api_author):
    #     mylogger.info("test for update some book by id with invalid author id")
    #     res_get_books = api_book.get_books()
    #     res_get_authors = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors)
    #     while True:
    #         num = random.randint(0, len(authors_id) + 1)
    #         if num not in authors_id:
    #             book = BookDto(res_get_books.json()[0]["name"], res_get_books.json()[0]["description"],
    #                                int(res_get_books.json()[0]["price"]), int(res_get_books.json()[0]["amountInStock"]),
    #                                res_get_books.json()[0]["imageUrl"], res_get_books.json()[0]["authorId"], num)
    #             res_put_book_id = api_book.put_book_byid(num, book)
    #             assert "Not Found" in res_put_book_id.text
    #             break
    #
    # def test_delete_book_byid(api_book):
    #     mylogger.info("test for delete some book by id")
    #     res_get_books = api_book.get_books()
    #     book_id = res_get_books.json()[0]["id"]
    #     res_delete_book = api_book.delete_book_byid(book_id)
    #     assert res_delete_book.status_code == 204
    #     res_get_book_byid = api_book.get_book_byid(book_id)
    #     assert "Not Found" in res_get_book_byid.text
    #
    # def test_delete_book_by_invalid_id(api_book):
    #     mylogger.info("test for delete some book with invalid id")
    #     res_get_books = api_book.get_books()
    #     books_id = all_authors_id(res_get_books)
    #     while True:
    #         num = random.randint(0, len(books_id) + 1)
    #         if num not in books_id:
    #             res_delete_book = api_book.delete_book_byid(num)
    #             assert "Not Found" in res_delete_book.text
    #             break
    #
    # def test_get_books_by_authorid(api_author, api_book):
    #     mylogger.info("test for get books by author id")
    #     res_get_author_id = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_author_id)
    #     author_id = authors_id[0]
    #     res = api_book.get_books_by_author_id(author_id)
    #     for book in res.json():
    #         assert book["authorId"] == author_id
    #
    # def test_get_books_by_invalid_authorid(api_book, api_author):
    #     mylogger.info("test for get books with no exist author id")
    #     res_get_authors = api_author.get_authors()
    #     authors_id = all_authors_id(res_get_authors)
    #     while True:
    #         num = random.randint(0, len(authors_id) + 1)
    #         if num not in authors_id:
    #             res = api_book.get_books_by_author_id(num)
    #             assert len(res.json()) == 0
    #             break
    #
    # def test_put_book_purchase_byid(api_book):
    #     mylogger.info("test for purchase book by id")
    #     res_get_books_id = api_book.get_books()
    #     books_id = all_books_id(res_get_books_id)
    #     res = api_book.put_book_purchase_byid(books_id[0])
    #     assert res_get_books_id.json()[0]["name"] in res.text
    #
    # def test_put_book_purchase_by_invalid_id(api_book):
    #     mylogger.info("test for purchase book with no exist id")
    #     res_get_books_id = api_book.get_books()
    #     books_id = all_books_id(res_get_books_id)
    #     while True:
    #         num = random.randint(0, len(books_id)+1)
    #         if num not in books_id:
    #             res = api_book.put_book_purchase_byid(num)
    #             assert "400 Bad Request - purchase unsucessful" in res.text
    #             break


if __name__ == '__main__':
    unittest.main()
