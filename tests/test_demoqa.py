import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Test data
TEST_FIRST_NAME = "Beimnet"
TEST_LAST_NAME = "Tadesse"
TEST_EMAIL = "beimnet@example.com"
TEST_MOBILE_VALID = "1234567890"
TEST_MOBILE_INVALID = "123456789"

# Helper function for human-like typing
def slow_type(element, text, delay=0.05):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

# Pytest Fixture
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# --- TC01: Valid Text Box Input ---
def test_tc01_text_box_valid(driver):
    driver.get("https://demoqa.com/text-box")
    
    name_field = driver.find_element(By.ID, "userName")
    email_field = driver.find_element(By.ID, "userEmail")
    
    slow_type(name_field, "Beimnet Tadesse")
    slow_type(email_field, "beimnet@example.com")
    
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    
    output = driver.find_element(By.ID, "output").text
    assert "Beimnet Tadesse" in output
    print("✅ TC01 PASSED: Valid input accepted")

# --- TC02: Invalid Email Format ---
def test_tc02_text_box_invalid_email(driver):
    driver.get("https://demoqa.com/text-box")
    
    driver.find_element(By.ID, "userName").send_keys("Test User")
    driver.find_element(By.ID, "userEmail").send_keys("invalid-email.com")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    
    output = driver.find_element(By.ID, "output").text
    # Invalid email should not appear correctly in output
    assert "invalid-email.com" not in output or "Email" not in output
    print("✅ TC02 PASSED: Invalid email handled")

# --- TC04: Practice Form Valid Submission ---
def test_tc04_practice_form_valid(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    
    # Fill required fields
    driver.find_element(By.ID, "firstName").send_keys(TEST_FIRST_NAME)
    driver.find_element(By.ID, "lastName").send_keys(TEST_LAST_NAME)
    driver.find_element(By.ID, "userEmail").send_keys(TEST_EMAIL)
    
    # Select Gender
    driver.find_element(By.XPATH, "//label[text()='Female']").click()
    
    # Enter mobile
    driver.find_element(By.ID, "userNumber").send_keys(TEST_MOBILE_VALID)
    
    # Scroll and submit
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    
    # Verify modal appears
    modal = driver.find_element(By.CLASS_NAME, "modal-content")
    assert modal.is_displayed()
    print("✅ TC04 PASSED: Form submitted successfully")