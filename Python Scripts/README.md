# Python Scripts

This folder contains my **standalone Python Selenium scripts**.  
They were my first automation attempts before moving to pytest.  
These scripts are run directly with the `python` command.

---

## Scripts
- `valid_login.py` → Automates valid login flow
- `invalid_login.py` → Automates invalid login flow

---

## What I Learned
- How to initialize and quit a WebDriver.
- How to locate elements using `By.ID`.
- Using `.send_keys()` to type into fields and `.click()` to interact with buttons.
- Writing basic `assert` statements for validation.
- The difference between running **individual scripts** with `python` vs running **test suites** with `pytest`.

---

## Resources I Used
Here are the main resources I referred to while building these scripts:

- **GeeksforGeeks Selenium with Python articles**  
  - [Writing Tests using Selenium in Python](https://www.geeksforgeeks.org/writing-tests-using-selenium-in-python/)
  - [Expected Conditions in Selenium with Types and Examples](https://www.geeksforgeeks.org/software-testing/expected-conditions-in-selenium-with-types-and-examples/)
  - [How to Automate Login using Selenium in Python](https://thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python)
 
  **Practice Application**  
  - [Sauce Demo](https://www.saucedemo.com/) — used as the test site.
