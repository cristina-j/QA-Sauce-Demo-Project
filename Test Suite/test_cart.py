import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_add_item_to_cart(valid_login):
    driver = valid_login


   # Add first item to the cart (original code: "driver.find_element..." but that caused an error. Fixed to say "driver.find_elements..." and indexing 0)
    product = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Make sure item name is captured 
    product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Click "Add to Cart" for the item
    product.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Open the cart to see item
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify that item added is in the cart  
    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item_name == product_name
