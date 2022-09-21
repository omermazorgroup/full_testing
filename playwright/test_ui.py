import time
import unittest

import pytest
from final_project.playwright.page_models.loginPage import LoginPage
from final_project.playwright.page_models.storePage import StorePage
from final_project.playwright.page_models.registerPage import RegisterPage
from final_project.playwright.page_models.basicPage import BasicPage
from final_project.playwright.page_models.authorsPage import AuthorsPage
from final_project.playwright.page_models.authorPage import AuthorPage
from final_project.playwright.page_models.searchPage import SearchPage
from playwright.sync_api import sync_playwright
import re
import logging
from threading import Event
import random
import string
from playwright.sync_api import Dialog
import sys
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()
# sys.argv[4] = './selenium/test_ui.py'
# mylogger.info(sys.argv[4])


# @pytest.fixture
# def register_user():
#     return {
#       "email": "admin@sela.co.il",
#       "password": "12345"
#     }


# @pytest.fixture
# def unregister_user():
#     return {
#       "email": "omer@sela.co.il",
#       "password": "35124"
#     }


def enter_main_page(playwright, url) -> BasicPage:
    """
    A function that go to main page
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.on('dialog', lambda dialog: dialog.accept())
    return BasicPage(page)


def enter_store_page(page):
    """
    A function that go to store page
    """
    return StorePage(page.click_store_link())


def open_login_page_and_submit(playwright, url, email: str, password: str):
    """
    A function that enter login page and submit the login form by two inputs which sent as parameters
    :param email: str, email input
    :param password: str, password input
    """
    main_page = enter_main_page(playwright, url)
    login_page = LoginPage(main_page.page)
    login_page.fill_email_input(email)
    login_page.fill_password_input(password)
    next_page = StorePage(login_page.click_sign_in())
    next_page.page.wait_for_timeout(2000)
    return next_page


def open_register_page_and_submit(url, email: str, password: str, firstname: str, lastname: str):
    """
    A function that enter to register page and submit the register form
    by register inputs which sent as parameters
    """
    with sync_playwright() as playwright:
        main_page = enter_main_page(playwright, url)
        login_page = LoginPage(main_page.page)
        register_page = RegisterPage(login_page.click_register_button())
        register_page.fill_email_input(email)
        register_page.fill_password_input(password)
        register_page.fill_firstname_input(firstname)
        register_page.fill_lastname_input(lastname)
        register_page.click_sign_up()
        register_page.page.wait_for_timeout(2000)
        return register_page


def enter_authors_page(page):
    """
    A function that go to authors page
    """
    return AuthorsPage(page.click_authors_link())


def enter_search_page(page, text):
    """
    A function that go to search page by clicking search button
    after filling the search input with some text
    :param text: str, A text to fill the search input
    """
    page.fill_search_input(text)
    page.click_search_button()
    return SearchPage(page.click_search_button())


def message_after_purchase(dialog, text: str):
    """
    A function that check if some text is inside dialog box
    :param text:str, A text to check
    """
    if not isinstance(text, str):
        raise TypeError("text parameter must be a string!")
    assert text in dialog.message


@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return f'{pytestconfig.getoption("url")}/'


@pytest.mark.usefixtures("driver_class")
class Tests(unittest.TestCase):
    # def __int__(self):
    #     self.login = None
    #     mylogger.info(444, self.login)

    # def test_method1(self):
    #     mylogger.info(self.login.url)
    def enter_main_page(self, playwright) -> BasicPage:
        """
        A function that go to main page
        """
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(self.driver.url)
        page.on('dialog', lambda dialog: dialog.accept())
        return BasicPage(page)

    def test_links(self):
        mylogger.info("test for the main links")
        with sync_playwright() as playwright:
            main_page = self.enter_main_page(playwright)
            store_page = StorePage(main_page.click_store_link())
            assert store_page.url() == "http://localhost/store"
            authors_page = AuthorsPage(main_page.click_authors_link())
            assert authors_page.url() == "http://localhost/authors"
            login_page = LoginPage(main_page.click_login_link())
            assert login_page.url() == "http://localhost/"

    def test_register_empty_email(self):
        mylogger.info("test for register with empty email input")
        register_page = open_register_page_and_submit(self.driver.url, "", self.driver.unregister_user["password"], "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_invalid_email(self):
        mylogger.info("test for register with invalid email input")
        register_page = open_register_page_and_submit(self.driver.url, "admin@", self.driver.unregister_user["password"], "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_shorter_password(self):
        mylogger.info("test for register with password input shorter than allowed")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], "123", "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_longer_password(self):
        mylogger.info("test for register with password input longer than allowed")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], "12345678910111213", "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_empty_password(self):
        mylogger.info("test for register with empty password input")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], "", "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_empty_firstname(self):
        mylogger.info("test for register with empty firstname input")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], self.driver.unregister_user["password"], "", "Mazor")
        assert register_page.url() == "http://localhost/register"

    def test_register_empty_lastname(self):
        mylogger.info("test for register with empty lastname input")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], self.driver.unregister_user["password"], "Omer", "")
        assert register_page.url() == "http://localhost/register"

    def test_register_registered_email(self):
        mylogger.info("test for register with registered user")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.register_user["email"], "24531", "Omer", "Mazor")
        assert register_page.url() == "http://localhost/register"

    @pytest.mark.skip(reason="No details about what happen after valid registration")
    def test_register_valid(self):
        mylogger.info("test for valid registration")
        register_page = open_register_page_and_submit(self.driver.url, self.driver.unregister_user["email"], self.driver.unregister_user["password"], "Omer", "Mazor")
        assert register_page.url() == "http://localhost/store"

    def test_login_empty_email(self):
        mylogger.info("test for login with empty email input")
        with sync_playwright() as playwright:
            next_page = open_login_page_and_submit(playwright, self.driver.url, "", self.driver.register_user["password"])
            assert next_page.url() == "http://localhost/"

    def test_login_invalid_email(self):
        mylogger.info("test for login with invalid email input")
        with sync_playwright() as playwright:
            next_page = open_login_page_and_submit(playwright, self.driver.url, "admin@", self.driver.register_user["password"])
            assert next_page.url() == "http://localhost/"

    def test_login_empty_password(self):
        mylogger.info("test for login with empty password input")
        with sync_playwright() as playwright:
            next_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.register_user["email"], "")
            assert next_page.url() == "http://localhost/"

    def test_login_unregistered_user(self):
        mylogger.info("test for login with unregistered user")
        with sync_playwright() as playwright:
            next_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.unregister_user["email"], self.driver.unregister_user["password"])
            assert next_page.url() == "http://localhost/"

    def test_login_registered_user(self):
        mylogger.info("test for login with registered user")
        with sync_playwright() as playwright:
            next_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.register_user["email"], self.driver.register_user["password"])
            assert next_page.url() == "http://localhost/store"

    def test_buy_book_without_login(self):
        mylogger.info("test for buy book without login")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            store_page = enter_store_page(main_page)
            store_page.page.wait_for_selector('.book-container')
            books = store_page.books_of_the_store()
            store_page.page.on('dialog', lambda dialog: message_after_purchase(dialog, "Must be signed in to purchase"))
            store_page.buy_book(random.randint(0, books.count()-1))

    def test_buy_book_with_login(self):
        mylogger.info("test for buy book with login")
        with sync_playwright() as playwright:
            store_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.register_user["email"], self.driver.register_user["password"])
            books = store_page.books_of_the_store()
            for num in range(books.count()):
                if store_page.book_amount(num) > 0:
                    store_page.page.on('dialog', lambda dialog: message_after_purchase(dialog, "Thank you for your purchase"))
                    starting_amount = store_page.book_amount(num)
                    store_page.buy_book(num)
                    # # assert "Thank you for your purchase" in store_page.message_after_purchase()
                    store_page.page.reload(timeout=0)
                    time.sleep(4)
                    assert starting_amount - 1 == store_page.book_amount(num)
                    break

    def test_buy_book_zero_amount(self):
        mylogger.info("test for buy book with 0 amount")
        with sync_playwright() as playwright:
            store_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.register_user["email"], self.driver.register_user["password"])
            books = store_page.books_of_the_store()
            for num in range(books.count()):
                if store_page.book_amount(num) == 0:
                    store_page.page.on('dialog',
                                       lambda dialog: message_after_purchase(dialog, "Thank you for your purchase"))
                    store_page.page.on('dialog',
                                       lambda dialog: message_after_purchase(dialog, "Request failed with status code 400"))
                    store_page.buy_book(num)
                    break

    def test_logout(self):
        mylogger.info("test for logout the user")
        with sync_playwright() as playwright:
            store_page = open_login_page_and_submit(playwright, self.driver.url, self.driver.register_user["email"], self.driver.register_user["password"])
            store_page.page.on('dialog', lambda dialog: message_after_purchase(dialog, "Must be signed in to purchase"))
            store_page.click_logout_button()
            books = store_page.books_of_the_store()
            store_page.buy_book(random.randint(0, books.count()-1))

    def test_link_to_author_page(self):
        mylogger.info("test for enter to some author page from store page")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            authors_page = enter_authors_page(main_page)
            authors = authors_page.authors_of_the_store()
            author = random.randint(0, authors.count()-1)
            author_name = authors_page.author_name(author)
            author_page = AuthorPage(authors_page.to_author_page(author))
            assert author_name == author_page.author_name()

    def test_books_of_author_in_author_page(self):
        mylogger.info("test for book in some author page")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            authors_page = enter_authors_page(main_page)
            authors = authors_page.authors_of_the_store()
            author = random.randint(0, authors.count()-1)
            author_page = AuthorPage(authors_page.to_author_page(author))
            # author_page.page.wait_for_selector('.book-container')
            books = author_page.author_books()
            for book in books.all_inner_texts():
                assert author_page.author_name() in book

    def test_valid_amount_author_books(self):
        mylogger.info("test for valid amount of books in some author page")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            authors_page = enter_authors_page(main_page)
            authors = authors_page.authors_of_the_store()
            author = random.randint(0, authors.count() - 1)
            author_page = AuthorPage(authors_page.to_author_page(author))
            author_name = author_page.author_name()
            author_books = author_page.author_books().count()
            store_page = enter_store_page(author_page)
            filtered = filter(lambda book: author_name in book, store_page.books_of_the_store().all_inner_texts())
            assert author_books == len(list(filtered))

    def test_empty_search_input(self):
        mylogger.info("test for search with empty search input")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            search_page = enter_search_page(main_page, "")
            search_page.page.wait_for_selector('.card-group')
            search_results = search_page.search_results()
            books = StorePage(search_page.click_store_link()).books_of_the_store().count()
            authors_and_books = books + AuthorsPage(search_page.click_authors_link()).authors_of_the_store().count()
            assert len(search_results) == authors_and_books

    def test_book_search(self):
        mylogger.info("test for search for some book")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            store_page = enter_store_page(main_page)
            books = store_page.books_of_the_store()
            book = random.randint(0, books.count()-1)
            book_name = store_page.book_name(book)
            search_page = enter_search_page(store_page, book_name)
            mylogger.info(books.count())
            search_results = search_page.search_results()
            assert len(search_results) < books.count()
            for result in search_results:
                assert book_name in result.inner_text()

    def test_author_search(self):
        mylogger.info("test for search for some author")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            authors_page = enter_authors_page(main_page)
            authors = authors_page.authors_of_the_store().count()
            author = random.randint(0, authors - 1)
            author_name = authors_page.author_name(author)
            search_page = enter_search_page(authors_page, author_name)
            search_results = search_page.search_results()
            assert len(search_results) < authors
            for result in search_results:
                assert author_name in result

    def test_fake_book_search(self):
        mylogger.info("test for search for some book that not exists in the system")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            store_page = StorePage(main_page.click_store_link())
            books = store_page.books_of_the_store()
            store_page.page.wait_for_selector('.book-container')
            books_names = []
            for index in range(books.count()):
                books_names.append(store_page.book_name(index))
            book_name = string.ascii_letters
            if book_name not in books_names:
                search_page = enter_search_page(store_page, book_name)
                search_results = search_page.search_results()
                assert len(search_results) == 0

    def test_fake_author_search(self):
        mylogger.info("test for search for some author that not exists in the system")
        with sync_playwright() as playwright:
            main_page = enter_main_page(playwright, self.driver.url)
            authors_page = enter_authors_page(main_page)
            authors = authors_page.authors_of_the_store()
            authors_page.page.wait_for_selector('.author-container')
            authors_names = []
            for index in range(authors.count()):
                authors_names.append(authors_page.author_name(index))
            author_name = string.ascii_letters
            if author_name not in authors_names:
                search_page = enter_search_page(authors_page, author_name)
                search_results = search_page.search_results()
                assert len(search_results) == 0


if __name__ == '__main__':
    unittest.main()
