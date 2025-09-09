from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the driver 
driver = webdriver.Chrome()

# Navigating to the login page
driver.get("https://www.saucedemo.com")
driver.maximize_window()

# Giving it a few second to open up
wait = WebDriverWait(driver, 20)

# Locating the login elements and interacting with it 
username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter valid login credentials for the website 
username_field.send_keys("invalid_username")
password_field.send_keys("wrong_password")
login_button.click()

# Check to make sure user stays on login page and an error message appears 
try: 
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message, f"Unexpected error message:{error_message}"
    assert "saucedemo.com" in driver.current_url and "inventory" not in driver.current_url, f"Unexpected URL: {driver.current_url}"

    print("Invalid login test passed")
    print("Error message:", error_message)

finally:
    driver.quit()
