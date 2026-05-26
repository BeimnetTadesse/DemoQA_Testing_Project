import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT_TIMEOUT)

    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Invalid')]")

    def navigate(self):
        self.driver.get(config.LOGIN_URL)

        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )

    def enter_username(self, username):
        el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        el = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))

        # IMPORTANT: real user-like click (NOT JS click)
        el.click()

    def login_with_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)

        if config.SLOW_MODE:
            time.sleep(1)  # teacher visibility

        self.click_login()

        if config.SLOW_MODE:
            time.sleep(2)  # allow UI transition

    def get_error_message(self):
        try:
            el = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return el.text.strip()
        except:
            return ""