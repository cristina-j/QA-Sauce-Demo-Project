import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# defining the functions - this is setting up the Webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# This is creating the function for validating the login flow

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

# Locating the login elements for Sauce Demo and interacting with it
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("invalid_username")
    password_field.send_keys("wrong_password")
    login_button.click()

# Need to add assertions

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message, f"Unexpected error message:{error_message}"

    assert "saucedemo.com" in driver.current_url and "inventory" not in driver.current_url, f"Unexpected URL: {driver.current_url}"
