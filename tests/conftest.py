import pytest

from utils import config
from utils.driver_factory import create_driver

from pages.login_page import LoginPage
from pages.bookstore_page import BookstorePage
from pages.profile_page import ProfilePage


@pytest.fixture(scope="function")
def driver():
    """
    Create Chrome driver instance and close after test.
    """

    driver = create_driver(headless=False)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def bookstore_page(driver):
    return BookstorePage(driver)


@pytest.fixture(scope="function")
def profile_page(driver):
    return ProfilePage(driver)