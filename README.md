# DemoQA Test Automation Framework

## 📌 Project Overview

This project is an automated testing framework developed for the **DemoQA Book Store application** as part of the SVVT course (Software Verification, Validation and Testing).

It demonstrates a **multi‑dimensional** testing approach:

- ✅ **UI Testing** with Selenium WebDriver
- ✅ **API Testing** with Requests + Pytest
- ✅ **Performance Testing** with Locust (50 concurrent users)
- ✅ **Security Testing** with OWASP ZAP (passive scan)

The framework validates frontend, backend, performance, and security posture of the DemoQA Book Store system.

---

## 🎯 Objectives

- Automate UI testing for login and book features
- Validate API endpoints for authentication and book CRUD operations
- Measure system performance under moderate load (50 users)
- Identify security misconfigurations (missing headers, information disclosure)
- Apply Page Object Model (POM) for maintainable UI automation
- Combine UI + API validation for reliable regression testing

---

## ⚙️ Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.11 | Main language |
| Selenium WebDriver | UI automation |
| Pytest | Test runner, assertions, HTML reporting |
| Requests | API testing |
| Locust | Performance / load testing |
| OWASP ZAP | Security scanning (passive) |
| WebDriver Manager | Automatic driver management |

---

## 📁 Project Structure
DemoQA/
├── pages/ → Page Object Models (login, profile, books)
├── tests/ → Test files (API, UI books, UI login)
├── utils/ → Configuration (URLs, credentials, constants)
├── performance/ → Locust load test script
├── reports/ → Generated HTML reports (pytest-html)
├── pytest.ini → Pytest configuration
├── requirements.txt → Python dependencies
└── README.md → This file

text

---

## 🧪 Test Coverage & Priorities

### Priority Definitions

| Priority | Meaning | When applied |
|----------|---------|--------------|
| **High** | Core functionality – must work for application to be usable | Authentication, book search, add/remove, valid login |
| **Medium** | Important but not critical – error handling, negative scenarios | Invalid login, empty fields, non‑existing search |
| **Low** | Edge cases – no security or data impact | Special characters in login |

---

### API Tests (7 tests) – `tests/test_api.py`

| TC_ID | Scenario | Priority | Status |
|-------|----------|----------|--------|
| TC_API_01 | Generate valid JWT token | **High** | ✅ Pass |
| TC_API_02 | Authorized check returns true | **High** | ✅ Pass |
| TC_API_03 | Get user profile | **High** | ✅ Pass |
| TC_API_04 | Add book to collection | **High** | ✅ Pass |
| TC_API_05 | Retrieve user books | **High** | ✅ Pass |
| TC_API_06 | Delete book from collection | **High** | ✅ Pass |
| TC_API_07 | Invalid login (negative) | **Medium** | ✅ Pass |

### UI Books Tests (5 tests) – `tests/test_books.py`

| TC_ID | Scenario | Priority | Status |
|-------|----------|----------|--------|
| TC_BOOKS_01 | Search existing book | **High** | ✅ Pass |
| TC_BOOKS_02 | Search non‑existing book | **Medium** | ✅ Pass |
| TC_BOOKS_03 | View book details | **High** | ✅ Pass |
| TC_BOOKS_04a | Add/remove Git Pocket Guide | **High** | ✅ Pass |
| TC_BOOKS_04b | Add/remove Speaking JavaScript | **High** | ✅ Pass |

### UI Login Tests (4 tests) – `tests/test_login.py`

| TC_ID | Scenario | Priority | Status |
|-------|----------|----------|--------|
| TC_LOGIN_01 | Valid credentials → profile redirect | **High** | ✅ Pass |
| TC_LOGIN_02 | Invalid password shows error | **Medium** | ✅ Pass |
| TC_LOGIN_03 | Empty fields show error | **Medium** | ✅ Pass |
| TC_LOGIN_04 | Special characters handled gracefully | **Low** | ✅ Pass |

### Performance Test (1 suite) – `performance/locustfile.py`

| Test | Configuration | Result |
|------|---------------|--------|
| Load test | 50 concurrent users, 2 min run, 5 users/sec ramp‑up | 0% failures, 95th %ile 6.7‑8.3s, 99th %ile 15‑18s |

### Security Scan (1 scan) – OWASP ZAP (passive)

| Scan type | Findings | Status |
|-----------|----------|--------|
| Passive scan (Traditional + AJAX Spider) | Missing CSP, HSTS, X‑Frame‑Options, X‑Content‑Type‑Options; no SQLi/XSS | Reported |

---

## 📊 Test Execution Summary (Final Run)

| Category | Number of Tests | Passed | Failed | Pass Rate |
|----------|----------------|--------|--------|-----------|
| API Tests | 7 | 7 | 0 | 100% |
| UI Books Tests | 5 | 5 | 0 | 100% |
| UI Login Tests | 4 | 4 | 0 | 100% |
| **Functional Tests Total** | **16** | **16** | **0** | **100%** |
| Performance Test | 1 suite | 0 failures | N/A | ✅ |
| Security Scan | 1 scan | No high‑risk findings | N/A | ✅ |

**Total execution time (functional tests):** ~4 minutes 27 seconds

---

## 🚀 How to Run Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run all functional tests (UI + API)
bash
pytest -v
3. Run specific test files
bash
# API tests only
pytest tests/test_api.py -v

# UI login tests only
pytest tests/test_login.py -v

# UI books tests only
pytest tests/test_books.py -v
4. Run a single test by name
bash
pytest tests/test_api.py::test_generate_token -v
5. Generate HTML report
bash
pytest --html=reports/report.html --self-contained-html
6. Run performance test (Locust)
bash
locust -f performance/locustfile.py --host https://demoqa.com
Then open http://localhost:8089 in your browser and start the test.

7. Run security scan (OWASP ZAP – manual)
Open OWASP ZAP

Click Automated Scan

Enter https://demoqa.com

Enable Traditional Spider and AJAX Spider

Click Attack

Review Alerts tab after completion.

⚠️ Known Issues & Observations
Issue	Severity	Workaround / Mitigation
Book cover images differ between books page and profile page	Low (cosmetic)	Report as UI inconsistency – no functional impact
/Account/v1/Authorized endpoint high latency under load (99th %ile 15‑18s)	High (performance)	Optimise with caching and database indexing (recommended)
Missing security headers (CSP, HSTS, X‑Frame‑Options, X‑Content‑Type‑Options)	Medium	Add headers in server configuration (recommended)
Shared sandbox data persists between runs	Low	Pre‑cleanup (DELETE before POST) implemented in test scripts
UI tests occasionally slow due to explicit waits	Low	Acceptable trade‑off for reliability; can be headless in CI
🧠 Key Design Decisions
Page Object Model (POM) – UI locators and actions are isolated in pages/ for maintainability.

Explicit waits – WebDriverWait replaces hardcoded sleep() for stability.

Fresh token per API test – Each test calls get_token() to avoid session expiry.

Pre‑cleanup for book tests – DELETE before POST prevents duplicate book errors in shared sandbox.

Separate API and UI authentication – API tests use direct token generation; UI tests use form login.

Performance test with gradual ramp‑up – 5 users/second simulates realistic traffic, avoids false failures.

Passive security scan only – Active scan omitted to protect shared sandbox.

📌 Author
Beimnet Tadesse (FTP 0217/15)
GitHub: https://github.com/BeimnetTadesse
Course: SWEG 5022 – Software Verification, Validation and Testing (SVVT)
Submitted to: Dr. Girma | April 23, 2026

🏁 Conclusion
This project delivers a complete, multi‑dimensional test automation framework for the DemoQA Book Store. It validates:

✅ Functional correctness (UI + API)

✅ Performance under moderate load (50 users)

✅ Security posture (passive scan, missing headers)

All 16 functional tests pass with 100% success rate. The framework is repeatable, well‑structured, and ready for integration into a CI/CD pipeline
