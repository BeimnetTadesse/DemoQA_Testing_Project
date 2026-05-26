import requests
from utils import config


def get_user_token(username, password):

    response = requests.post(
        f"{config.API_BASE_URL}/Login",
        json={
            "userName": username,
            "password": password
        }
    )

    data = response.json()

    token = data.get("token")
    user_id = data.get("userId")

    print("🔐 API TOKEN:", token)
    print("🆔 API USER ID:", user_id)

    return user_id, token