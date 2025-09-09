import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# defining the functions - this is setting up the Webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# This is creating the function for validating the login flow

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

# Locating the login elements for Sauce Demo and interacting with it
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

# Need to add assertions

    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

    products_heading = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert products_heading.text == "Products"

    wait.until(EC.title_is("Swag Labs"))
    assert driver.title == "Swag Labs"
