# SauceDemo – Pytest Automation Suite

This folder contains an automated test suite for the SauceDemo site using Selenium and Pytest.  
It complements the manual artifacts in `test cases for sauce demo site` (test cases, execution logs, and test plan).

## What’s Included
- `saucedemo_tests/`
  - `conftest.py`: shared fixtures for WebDriver and login
  - `test_login.py`: valid login tests
  - `test_login_invalid_password.py`: validates that wrong password cannot be used
  - `test_login_invalid_username.py`: validates that wrong username cannot be used
  - `test_cart.py`: add-to-cart verification

**Note**: I will be adding a test checkout process to this test suite.
