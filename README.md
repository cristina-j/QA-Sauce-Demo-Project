# QA Project – Sauce Demo Login Flow

This project focuses on testing the **login functionality** of the [Sauce Demo](https://www.saucedemo.com/) sample web application.  
It showcases my complete QA workflow: from **exploratory testing** and planning, through **manual test documentation**, to **automation** of repetitive login scenarios with Selenium and Python.

---

## My Approach & Workflow

### 1. Exploratory Testing
I began by exploring the Sauce Demo site manually:
- Observed the login screen layout (username, password fields, login button).
- Identified possible test ideas:
  - Valid login with correct credentials
  - Invalid login with incorrect credentials
  - Edge cases like blank fields, etc.
- Noted expected behaviors for each scenario.

Exploratory testing helped me decide what would be **most important to document and automate** and it gave me more insight into what the website is supposed to do.

---

### 2. Test Planning
I created a **Test Plan** to define:
- **Scope:** Only the login functionality was tested in this project.
- **Objectives:** Verify login works with valid credentials, and is properly restricted for invalid credentials.
- **Risks:** Login failures could block users from accessing the site.
- **Environment:** Browser-based testing on Chrome (desktop).
- **Entry/Exit Criteria:** Login feature implemented and accessible; tests complete when all planned cases are executed and major defects resolved.

---

### 3. Test Case Design
I documented test cases in a structured **Test Case Log**:
- **Valid login:** Expected successful redirection to the Products page.
- **Invalid login:** Expected error message and no redirection.
- **Additional considerations:** Blank username, blank password, multiple failed attempts.

---

### 4. Test Execution
I executed my test cases manually, recording results in a **Test Execution Log**:
- Linked defects where necessary (if behavior did not match expectations).

---

### 5. Automation
To save time on repetitive login tests, I automated:
- **Valid login flow**
- **Invalid login flow**

Automation was chosen here because:
- Login is a critical, repetitive task.
- Automating ensures consistency and saves manual effort for regression.

## Automated Test Scripts:

- `test_valid_login.py` → Logs in with valid credentials and verifies:
  - URL contains `inventory`
  - Page heading = `Products`
  - Browser title = `Swag Labs`

- `test_invalid_login.py` → Attempts login with invalid credentials and verifies:
  - User remains on login page
  - Error message appears:  
    *Epic sadface: Username and password do not match any user in this service*
  - URL does not redirect to `inventory.html`
