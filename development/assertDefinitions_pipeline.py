import pytest
import time
from environments import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from environments import *
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Elements import *
from selenium.webdriver.common.keys import Keys

fail_message = "fail_message"
pass_message = "This test has passed"
type = ""
element = ""
value = ""

def pauseBetweenActions():
        time.sleep(1)
        driver.implicitly_wait(60)

# environments
@pytest.fixture
def chrome_environment_setup():
        global driver
        driver= webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
    
        pauseBetweenActions() # ensure_all_first_requests_end
        
# assert_functions
def assert_page_title(element):
        pauseBetweenActions()
        try:
                title = driver.title
                assert element in title
                print(pass_message)
                print(title)
        except Exception as e:
                print(fail_message, format(e))
                print(title)
                
def assert_product_is_in_cart(element):
        pauseBetweenActions()
        try:    #WIP TO BE DEVELOPED
                title = driver.title
                assert element in title
                print(pass_message)
                print(title)
        except Exception as e:
                print(fail_message, format(e))
                print(title)

def assert_product_qty_in_cart(product_id, variant_id, unit_id, quantity):
        pauseBetweenActions()
        try:
                product_selector = get_orderline_key(product_id, variant_id, unit_id)
                quantity_field_selector = product_selector + " " + Elements.quantity_field
                
                driver.find_element(By.CSS_SELECTOR(quantity_field_selector), value=quantity)
                print("you have added " + quantity + " products to the cart")
                assert(True)
                
        except Exception as e:
                print(fail_message, format(e))
                assert(False)
                
def assert_product_price_in_cart(product_id, variant_id, unit_id, product_unit_price, quantity):
        pauseBetweenActions()
        try: #WIP TO BE DEVELOPED
                product_selector = get_orderline_key(product_id, variant_id, unit_id)
                orderline_total_price = getattr(product_selector, Elements.orderline_total_price)
                total_price = product_unit_price * quantity
                
                if total_price == orderline_total_price:
                        print(pass_message)
                        assert(True)
                else:
                        print(fail_message)
                        assert(False)

                assert_page_has_errors()
					
        except Exception as e:
                print(fail_message, format(e))
                assert(False)
                
def assert_page_has_errors():
        pauseBetweenActions()
        elementObject = driver.find_element_by_partial_link_text("An error occurred while attaching module")
        
        if elementObject:
                print(fail_message)
                assert(False)
        
def get_orderline_key(product_id, variant_id, unit_id):
        return "[data-product-id=\"" + product_id + "\"][data-variant-id]=\"" + variant_id + "\"[data-unit-id]=\"" + unit_id + "\""

def send_keys(element, value):
        pauseBetweenActions()
        elementObject = driver.find_element(By.CSS_SELECTOR, element)
        
        if elementObject:
                elementObject.send_keys(value)
        else:
                print(fail_message)
                assert(False)
                          
def click(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(By.CSS_SELECTOR, element)
        
        if elementObject:
                driver.execute_script("arguments[0].click();", elementObject)
        else:
                print(fail_message)
                assert(False)

def click_cookies(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(By.CSS_SELECTOR, element)
        
        if elementObject:
                elementObject.click()
                
        else:
                print(fail_message)
                assert(False)              

def clear_field(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(By.CSS_SELECTOR, element)
        
        if elementObject:
                elementObject.clear()
        else:
                print(fail_message)
                assert(False) 
                         
def partial_link_text(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(By.PARTIAL_LINK_TEXT, element)
        
        if elementObject:
                driver.execute_script("arguments[0].click();", elementObject)
        else:
                print(fail_message)
                assert(False)

def click_by_xpath(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(By.XPATH, element)
        
        if elementObject:
                elementObject.click()
        else:
                print(fail_message)
                assert(False)

def quit_browser():
        pauseBetweenActions() 
        driver.quit()

def back():
        pauseBetweenActions() 
        driver.back()