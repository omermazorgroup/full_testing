import pytest
import logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost")
    parser.addoption("--framework", action="store", default="selenium")
    parser.addoption("--browser", action="store", default="chrome")
    # sys.argv[5] = f'./selenium/test_ui.py'


@pytest.fixture(scope="session")
def unregister_user():
    return {
      "email": "omer@sela.co.il",
      "password": "35124"
    }


@pytest.fixture(scope="session")
def register_user():
    return {
      "email": "admin@sela.co.il",
      "password": "12345"
    }


@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return f'{pytestconfig.getoption("url")}/'


@pytest.fixture(scope="session")
def framework(pytestconfig) -> str:
    """
    give the framework from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: framework to integrate
    """
    return pytestconfig.getoption("framework")


@pytest.fixture(scope="session")
def browser(pytestconfig) -> str:
    """
    give the framework from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: framework to integrate
    """
    return pytestconfig.getoption("browser")


@pytest.fixture(scope="class")
def driver_class(request, url, framework, browser, unregister_user, register_user):
    class Driver:
        def __init__(self):
            self.url = url
            self.framework = framework
            self.unregister_user = unregister_user
            self.register_user = register_user
            self.browser = browser
    request.cls.driver = Driver()

