import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookstorePage:

    SEARCH_INPUT = (By.ID, "searchBox")
    BOOK_LINKS = (By.CSS_SELECTOR, ".action-buttons a")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add To Your Collection']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ---------------- NAVIGATE ----------------
    def navigate(self):
        self.driver.get("https://demoqa.com/books")
        self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))

    # ---------------- SEARCH ----------------
    def search_book(self, keyword):
        print(f"🔎 Searching: {keyword}")

        box = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )

        box.clear()
        box.send_keys(keyword)

        time.sleep(2)

    # ---------------- GET TITLES ----------------
    def get_book_titles(self):
        time.sleep(1)

        links = self.driver.find_elements(*self.BOOK_LINKS)
        titles = [l.text.strip() for l in links if l.text.strip()]

        print(f"📦 Found: {len(titles)} books")
        print("📚 Titles:", titles)

        return titles

    # ---------------- CLICK BOOK ----------------
    def click_book(self, title):

        print(f"📖 Clicking: {title}")

        self.wait.until(EC.presence_of_all_elements_located(self.BOOK_LINKS))

        time.sleep(2)

        links = self.driver.find_elements(*self.BOOK_LINKS)

        target = None
        for link in links:
            if title.lower() in link.text.lower():
                target = link
                break

        assert target is not None, "Book not found"

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            target
        )

        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", target)

        time.sleep(2)

        print("✅ Book clicked")

    # ---------------- STORAGE FIX (IMPORTANT) ----------------
    def get_local_storage_credentials(self):

    # wait until storage is actually populated
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        time.sleep(2)

        token = self.driver.execute_script("""
            return localStorage.getItem('token')
                || sessionStorage.getItem('token');
        """)

        user_id = self.driver.execute_script("""
            return localStorage.getItem('userId')
                || localStorage.getItem('userID')
                || sessionStorage.getItem('userId')
                || sessionStorage.getItem('userID');
        """)

        print("🔐 TOKEN:", token)
        print("🆔 USER ID:", user_id)

        return user_id, token