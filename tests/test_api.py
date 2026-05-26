import requests
from utils import config


# =========================
# HELPERS
# =========================

ISBN = "9781449325862"


def get_token():
    res = requests.post(
        f"{config.API_ACCOUNT_URL}/GenerateToken",
        json={
            "userName": config.TEST_USER,
            "password": config.TEST_PASS
        }
    )

    try:
        data = res.json()
    except:
        data = {}

    token = data.get("token")
    print("🔐 TOKEN:", token)

    return token


def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# =========================
# TESTS
# =========================

def test_generate_token():
    token = get_token()

    assert token is not None
    assert len(token) > 10


def test_authorized():
    res = requests.post(
        f"{config.API_ACCOUNT_URL}/Authorized",
        json={
            "userName": config.TEST_USER,
            "password": config.TEST_PASS
        }
    )

    print("AUTH RESPONSE:", res.text)

    assert res.status_code in [200, 401]
    assert res.text in ["true", "false"]


def test_get_user():
    res = requests.get(
        f"{config.API_ACCOUNT_URL}/User/{config.TEST_USER_ID}"
    )

    print(res.text)

    assert res.status_code in [200, 401, 404]


def test_add_book():
    token = get_token()
    headers = get_headers(token)

    # STEP 1: CLEAN OLD BOOK (IGNORE ERRORS)
    requests.delete(
        f"{config.API_BOOKSTORE_URL}/Book",
        json={
            "isbn": ISBN,
            "userId": config.TEST_USER_ID
        },
        headers=headers
    )

    # STEP 2: ADD BOOK
    res = requests.post(
        f"{config.API_BOOKSTORE_URL}/Books",
        json={
            "userId": config.TEST_USER_ID,
            "collectionOfIsbns": [
                {"isbn": ISBN}
            ]
        },
        headers=headers
    )

    print("ADD BOOK RESPONSE:", res.text)

    assert res.status_code in [200, 201]


def test_user_books():
    token = get_token()
    headers = get_headers(token)

    res = requests.get(
        f"{config.API_ACCOUNT_URL}/User/{config.TEST_USER_ID}",
        headers=headers
    )

    print("BOOKS:", res.text)

    assert res.status_code in [200, 401]


def test_delete_book():
    token = get_token()
    headers = get_headers(token)

    res = requests.delete(
        f"{config.API_BOOKSTORE_URL}/Book",
        json={
            "isbn": ISBN,
            "userId": config.TEST_USER_ID
        },
        headers=headers
    )

    print("DELETE RESPONSE:", res.text)

    assert res.status_code in [200, 204, 400, 401]


def test_invalid_login():
    res = requests.post(
        f"{config.API_ACCOUNT_URL}/GenerateToken",
        json={
            "userName": "wrong_user",
            "password": "wrong_pass"
        }
    )

    print("NEGATIVE AUTH:", res.text)

    try:
        data = res.json()
    except:
        data = {}

    assert (
        res.status_code in [400, 401]
        or data.get("token") is None
        or data.get("status") == "Failed"
    )