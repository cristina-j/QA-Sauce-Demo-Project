import pytest 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_login_invalid_password(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Using the correct username, but wrong password
    driver.find_element(By.ID, "user-name").send_keys("wrong_username")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # User would need to click the login button 
    driver.find_element(By.ID, "login-button").click()

    # Need to make sure the error message appears
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "do not match" in error.text
