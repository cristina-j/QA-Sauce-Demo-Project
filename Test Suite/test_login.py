import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test__valid_login(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")


    username_element = "user-name" 
    find_element = driver.find_element(By.ID, "user-name")
    find_element.send_keys("standard_user")

    password_element = "password"
    find_element_password = driver.find_element(By.ID, "password")
    find_element_password.send_keys("secret_sauce")
    find_element.send_keys(Keys.ENTER)
