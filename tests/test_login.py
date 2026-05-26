import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from utils import config


def test_login_success(driver, login_page, profile_page):

    login_page.navigate()
    login_page.login_with_credentials(config.TEST_USER, config.TEST_PASS)

    # DEBUG: show what actually happened
    print("URL AFTER LOGIN:", driver.current_url)

    WebDriverWait(driver, 10).until(
        lambda d: "profile" in d.current_url or "login" in d.current_url
    )

    assert "profile" in driver.current_url.lower()

    if config.SLOW_MODE:
        time.sleep(3)

    username_displayed = profile_page.get_logged_in_username()
    assert username_displayed == config.TEST_USER

    print("✅ LOGIN SUCCESS TEST PASSED")


def test_login_failure_invalid_credentials(driver, login_page):

    login_page.navigate()
    login_page.login_with_credentials("invalid_user_xyz", "WrongPassword123")

    time.sleep(1)

    assert "profile" not in driver.current_url.lower()

    err = login_page.get_error_message()
    assert "Invalid" in err

    print("✅ INVALID LOGIN PASSED")


def test_login_failure_empty_credentials(driver, login_page):

    login_page.navigate()
    login_page.login_with_credentials("", "")

    time.sleep(1)

    assert "profile" not in driver.current_url.lower()

    print("✅ EMPTY LOGIN PASSED")


def test_login_with_special_characters(driver, login_page):

    login_page.navigate()
    login_page.login_with_credentials("@#$%^", "Rahel@123")

    time.sleep(1)

    assert (
        "profile" in driver.current_url.lower()
        or "login" in driver.current_url.lower()
    )

    print("✅ SPECIAL CHAR TEST PASSED")