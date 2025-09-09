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
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Checking to make sure the correct page appears once user logs in successfully 

# First check that user is on the inventory page
wait.until(EC.url_contains("inventory"))
assert "inventory" in driver.current_url, f"Unexpected URL: {driver.current_url}"

# Check the heading of the page, making sure it is "Products"
products_heading = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
assert products_heading.text == "Products", f"Expected 'Products', got {products_heading.text}"

# Check the browser title is "Swag Labs"

expected_title = "Swag Labs"
assert driver.title == expected_title, f"Login failed. Expected title: {expected_title}, Actual title:{driver.title}"

# Check that the "Products" heading is visible
wait.until(EC.title_is("Swag Labs"))
assert driver.title == "Swag Labs", f"Unexpected title: {driver.title}"

print("Login test passed")
print("Page Heading:", products_heading.text)
print("Title:", driver.title)
print("URL:", driver.current_url)


#closing the webdriver
driver.quit()
