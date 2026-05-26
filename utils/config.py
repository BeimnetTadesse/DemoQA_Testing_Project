import os

# Base Application configurations
BASE_URL = "https://demoqa.com"
LOGIN_URL = f"{BASE_URL}/login"
BOOKS_URL = f"{BASE_URL}/books"
PROFILE_URL = f"{BASE_URL}/profile"

# API Base Configurations
API_BASE_URL = "https://bookstore.toolsqa.com"
API_ACCOUNT_URL = f"{API_BASE_URL}/Account/v1"
API_BOOKSTORE_URL = f"{API_BASE_URL}/BookStore/v1"

# Test Credentials (DemoQA Shared Sandbox Account)
# NOTE: If this account is deleted or modified, users can register a new one.
TEST_USER = "testuser123"
TEST_PASS = "Test@123"
TEST_USER_ID = "8e7582c2-50a4-40d9-9f44-22e9569b7d81"

# System Execution Delay Settings

HEADLESS = False

SLOW_MODE = True
TYPING_DELAY = 0.01
DEMO_DELAY = 1.5
IMPLICIT_WAIT_TIMEOUT = 10
EXPLICIT_WAIT_TIMEOUT = 15
