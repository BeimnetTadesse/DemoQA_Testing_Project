from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    USERNAME_LABEL = (By.ID, "userName-value")

    def get_logged_in_username(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_LABEL)
        )
        return el.text.strip()