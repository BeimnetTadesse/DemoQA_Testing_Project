
# DemoQA Test Automation Framework

## 📌 Project Overview

This project is an automated testing framework developed for the **DemoQA Book Store application** as part of the SVVT course (Software Verification, Validation and Testing).

It demonstrates a hybrid automation approach using:

* UI Testing with Selenium WebDriver
* API Testing with Requests + Pytest
* Page Object Model (POM) design pattern

The framework validates both frontend and backend functionality of the DemoQA Book Store system.

---

## 🎯 Objectives

* Automate UI testing for login and book features
* Validate API endpoints for authentication and book operations
* Ensure functional correctness using structured test cases
* Apply Page Object Model for scalable automation design
* Combine UI + API validation for better test reliability

---

## ⚙️ Tech Stack

* Python 3.11
* Selenium WebDriver
* Pytest
* Requests
* WebDriver Manager

---

## 📁 Project Structure

```
pages/        → Page Object Models (Login, Profile, Books)
tests/        → UI and API test cases
utils/        → Configuration (URLs, credentials, constants)
pytest.ini    → Pytest configuration
```

---

## 🧪 Test Coverage

### 🔵 UI Tests (Selenium)

#### Login Module (4 Tests)

Located in:

```
tests/test_login.py
```

Covered Scenarios:

* Valid login redirects to profile page
* Invalid login shows error message
* Empty credentials handling
* Special character login behavior

---

#### Books Module (4 Tests)

Located in:

```
tests/test_books.py
```

Covered Scenarios:

* Search existing book
* Search non-existing book
* View book details
* Add / remove book flow (UI-based)

---

### 🟢 API Tests (Requests + Pytest)

#### API Module (7 Tests)

Located in:

```
tests/test_api.py
```

Covered Scenarios:

* Generate authentication token
* Authorized user check
* Get user details
* Add book to collection
* Get user books
* Delete book from collection
* Negative login validation

---

## 📊 Test Summary

| Category         | Total Tests | Passed | Failed | Status     |
| ---------------- | ----------- | ------ | ------ | ---------- |
| UI Tests (Login) | 4           | 4      | 0      | ✅ Pass     |
| UI Tests (Books) | 4           | 3      | 1      | ⚠️ Partial |
| API Tests        | 7           | 7      | 0      | ✅ Pass     |

### **Total Tests: 15**

### **Overall Pass Rate: ~93.3%**

---

## 🚀 How to Run Tests

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run all tests

```bash
pytest -v
```

---

### Run UI tests only

```bash
pytest tests/test_login.py -v
pytest tests/test_books.py -v
```

---

### Run API tests only

```bash
pytest tests/test_api.py -v
```

---

### Generate HTML report

```bash
pytest --html=reports/report.html
```

---

## ⚠️ Known Issues

* DemoQA is a public sandbox and may behave inconsistently
* UI add/remove book flow may fail due to session/localStorage issues
* Some UI state updates require manual refresh
* API tests remain the most stable validation layer

These are environment limitations, not framework defects.

---

## 🧠 Key Design Decisions

* Page Object Model used for maintainability
* Explicit waits used for UI stability
* Hybrid UI + API testing approach for reliability
* API layer used as fallback validation for unstable UI behavior

---

## 📌 Author

**Beimnet Tadesse**
GitHub: [https://github.com/BeimnetTadesse](https://github.com/BeimnetTadesse)

---

## 🏁 Conclusion

This project demonstrates a complete automation testing framework including:

* UI automation testing (Login + Books)
* API automation testing
* Structured test design using Pytest
* Real-world QA engineering practices

It validates both frontend and backend behavior of the DemoQA Book Store application.

---
 
