# DemoQA Automated Testing Project 🧪

**Course:** SWEG 5022 - Software Verification, Validation and Testing (Assignment II)  
**Application Tested:** https://demoqa.com  
**Framework:** Selenium WebDriver (Python) + Pytest  
**Repository:** https://github.com/BeimnetTadesse/DemoQA_Testing_Project  

---

## 📌 Project Description

This project demonstrates automated functional testing of a web application using Selenium WebDriver and Pytest.

This repository contains the automated test suite for the SVVT Individual Software Testing Project. The purpose is to apply software testing techniques such as **Equivalence Partitioning**, **Boundary Value Analysis**, and **Decision Table Testing** on the DemoQA practice automation website.

The test cases cover core modules including **Text Box** and **Practice Form**, ensuring functional validation of user input handling and form submission behavior.

---

## 🧪 Test Coverage Summary

| Test Case | Module        | Description                         | Result            |
|-----------|--------------|-------------------------------------|------------------|
| TC01      | Text Box      | Valid name + email input            | ✅ PASS          |
| TC02      | Text Box      | Invalid email format validation     | ✅ PASS          |
| TC03      | Text Box      | Empty submission                    | ✅ PASS (manual) |
| TC04      | Practice Form | Complete valid submission           | ✅ PASS          |
| TC05      | Practice Form | Missing First Name validation       | ✅ PASS (manual) |
| TC06      | Practice Form | Mobile number input validation      | ✅ PASS          |

**Pass Rate:** 100% (6/6 tests passed)

---

## 🛠️ Technology Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | Programming language |
| Selenium WebDriver | 4.43 | Browser automation |
| Pytest | 7.4+ | Test framework |
| WebDriver Manager | 4.0+ | Driver management |

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/BeimnetTadesse/DemoQA_Testing_Project.git
cd DemoQA_Testing_Project
```

### 2. Create virtual environment
```bash
python3 -m venv venv
```

### 3. Activate environment

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest tests/test_demoqa.py -v
```

### Generate HTML report
```bash
pytest tests/test_demoqa.py --html=report.html --self-contained-html
```

---

## 📂 Repository Structure

```
DemoQA_Testing_Project/
├── tests/
│   └── test_demoqa.py
├── requirements.txt
├── report.html
└── README.md
```

---

## 📋 Test Design Techniques Applied

| Technique                | Application                                 |
|--------------------------|---------------------------------------------|
| Equivalence Partitioning | Email validation (valid vs invalid formats) |
| Boundary Value Analysis  | Mobile number input validation              |
| Decision Table Testing   | Form submission rules                       |

---

## 👤 Author

**Beimnet Tadesse**  
FTP 0217/15  
SWEG 5022 - SVVT Assignment II  
Date: April 23, 2026  

---