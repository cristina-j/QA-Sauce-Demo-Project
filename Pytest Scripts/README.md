# Pytest Scripts

This folder contains my **pytest-based automation scripts**.  
These are more professional than plain Python scripts because pytest:
- Automatically discovers test files and functions.
- Runs multiple tests in a single command.
- Provides clear pass/fail reporting.
- Can be extended with fixtures, plugins, and command-line options.

---

## Scripts
- `test_valid_login.py` → Valid login should redirect to the Products page
- `test_invalid_login.py` → Invalid login should stay on login page with error message

---

## What I Learned About Pytest
- **What pytest is:**  
  Pytest is a Python testing framework that makes it easy to write small, readable tests and scale them to larger suites.

**Why use pytest in QA automation:**  

- With regular Python scripts, I have to run each script one by one using python script.py, but with pytest I can run all of my tests at once with a single command: `pytest -q`.
- It gives me clear results in the terminal (like `PASSED`, `FAILED`, or `ERROR`), which looks more professional than just using print statements.
- I like that I can use fixtures (for example, setting up and quitting the driver), which makes the code cleaner and I don’t have to repeat the same setup in every test.
- It works really well with Selenium, so it’s a natural fit as I’m learning automation.
- Plus, it’s free and open source, so anyone can use it.

**When to use pytest:**  
- If I want my tests to be repeatable and easy to maintain over time.
- If I want to run both positive and negative test cases together in one batch.
- If I want to scale up my automation — instead of just running one login script, I can run a whole suite of different tests in one go.


## Issues I Encountered for `test_valid_login.py` and How I Fixed Them
1. **Wrong import case**  
   - `from Selenium.webdriver.common.by import By`  
   - Fixed to `from selenium.webdriver.common.by import By`

2. **WebDriver initialization error**  
   - `webdriver.Chrome(ChromeDriverManager().install())` → gave `'str' object has no attribute capabilities'`  
   - Fixed by using a `Service`:  
     ```python
     from selenium.webdriver.chrome.service import Service
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     ```

3. **Typo in valid credentials**  
   - `"secret-sauce"` 
   - Corrected to `"secret_sauce"`

4. **Pytest didn’t run tests**  
   - Cause: File was named `automating_login.py` and function `valid_login()`.  
   - Renamed the file to `test_valid_login.py` and function to `test_valid_login()` so pytest could know what it was going to test.

5. **Indentation error in invalid login test**  
   - Misaligned `wait.until(...)`  
   - Fixed indentation so assertions are inside the test function.
