import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")

    username_element = "user-name"
    find_element = driver.find_element(By.ID, "user-name")
    find_element.send_keys("wrongusername")

    password_element = "password"
    find_element = driver.find_element(By. ID, "password")
    find_element.send_keys("wrongpassword")
    find_element.send_keys(Keys.ENTER)

    error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    error_message_element = error_element.text

    assert "Epic sadface" in error_message_element
