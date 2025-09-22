# This file will have all the necessary tests fixtures here that will always need to be a part of a test. 
# This way I don't have to write it every time I am testing a new feature that needs to go through either starting the browser 
# or signing in.
# There will be athough fixtures added as needed

import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# This is is a fixture for starting and stopping the browser

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    yield driver 
    driver.quit()

# This is a fixture to start the browser and login in with valid credentials

@pytest.fixture
def valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    return driver
