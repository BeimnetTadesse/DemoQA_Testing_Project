import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from utils import config


# =========================
# HELPERS
# =========================

def get_auth_data():

    # GENERATE TOKEN
    token_res = requests.post(
        f"{config.API_ACCOUNT_URL}/GenerateToken",
        json={
            "userName": config.TEST_USER,
            "password": config.TEST_PASS
        }
    )

    token_data = token_res.json()

    token = token_data.get("token")

    print("🔐 TOKEN:", token)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # GET USER INFO
    user_res = requests.get(
        f"{config.API_ACCOUNT_URL}/User/{config.TEST_USER_ID}",
        headers=headers
    )

    print("👤 USER RESPONSE:", user_res.text)

    user_data = user_res.json()

    user_id = user_data.get("userId")

    print("🆔 USER ID:", user_id)

    return token, user_id


# =========================
# SEARCH EXISTING BOOK
# =========================

def test_search_existing_book(driver, bookstore_page):

    bookstore_page.navigate()

    bookstore_page.search_book("Git")

    titles = bookstore_page.get_book_titles()

    assert len(titles) > 0
    assert any("Git" in t for t in titles)

    print("✅ SEARCH TEST PASSED")


# =========================
# SEARCH NON EXISTING BOOK
# =========================

def test_search_non_existing_book(driver, bookstore_page):

    bookstore_page.navigate()

    bookstore_page.search_book("FakeBook123456")

    titles = bookstore_page.get_book_titles()

    assert all("FakeBook123456" not in t for t in titles)

    print("✅ NO RESULT TEST PASSED")


# =========================
# VIEW BOOK DETAILS
# =========================

def test_view_book_details(driver, bookstore_page):

    bookstore_page.navigate()

    bookstore_page.search_book("Git Pocket Guide")

    bookstore_page.click_book("Git Pocket Guide")

    time.sleep(2)

    print("✅ VIEW BOOK TEST PASSED")


# =========================
# ADD + REMOVE BOOK FLOW
# =========================
def test_add_and_remove_book_flow(
    driver,
    login_page,
    bookstore_page,
    profile_page
):

    target_book = "Git Pocket Guide"
    target_isbn = "9781449325862"

    # =========================
    # LOGIN UI
    # =========================

    login_page.navigate()

    login_page.login_with_credentials(
        config.TEST_USER,
        config.TEST_PASS
    )

    WebDriverWait(driver, 20).until(
        lambda d: "profile" in d.current_url.lower()
    )

    print("✅ LOGIN SUCCESS")

    time.sleep(5)

    # =========================
    # GET TOKEN FROM API
    # =========================

    token_res = requests.post(
        f"{config.API_ACCOUNT_URL}/GenerateToken",
        json={
            "userName": config.TEST_USER,
            "password": config.TEST_PASS
        }
    )

    token = token_res.json().get("token")

    print("🔐 TOKEN:", token)

    user_id = config.TEST_USER_ID

    print("🆔 USER ID:", user_id)

    assert token is not None

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # =========================
    # CLEAN OLD BOOK
    # =========================

    requests.delete(
        f"{config.API_BOOKSTORE_URL}/Book",
        json={
            "isbn": target_isbn,
            "userId": user_id
        },
        headers=headers
    )

    print("🧹 OLD BOOK CLEANED")

    time.sleep(2)

    # =========================
    # ADD BOOK THROUGH API
    # =========================

    response = requests.post(
        f"{config.API_BOOKSTORE_URL}/Books",
        json={
            "userId": user_id,
            "collectionOfIsbns": [
                {
                    "isbn": target_isbn
                }
            ]
        },
        headers=headers
    )

    print("➕ ADD RESPONSE:", response.text)

    assert response.status_code in [200, 201]

    print("✅ BOOK ADDED")

    # =========================
    # MANUAL AUTH FIX
    # =========================

    driver.get(config.BASE_URL)

    time.sleep(3)

    driver.execute_script(f"""
        window.localStorage.setItem('token', '{token}');
        window.localStorage.setItem('userID', '{user_id}');
        window.localStorage.setItem('userName', '{config.TEST_USER}');
    """)

    print("✅ LOCAL STORAGE AUTH INJECTED")

    time.sleep(3)

    # =========================
    # OPEN PROFILE
    # =========================

    driver.get(config.PROFILE_URL)

    time.sleep(10)

    driver.refresh()

    time.sleep(5)

    books = profile_page.get_profile_books()

    print("📚 PROFILE BOOKS:", books)

    assert target_book in books

    print("✅ BOOK FOUND IN PROFILE")

    # =========================
    # DELETE BOOK USING UI
    # =========================

    profile_page.delete_book(target_book)

    print("🗑 DELETE CLICKED")

    time.sleep(5)

    driver.refresh()

    time.sleep(5)

    books_after = profile_page.get_profile_books()

    print("📚 AFTER DELETE:", books_after)

    assert target_book not in books_after

    print("✅ REMOVE TEST PASSED")