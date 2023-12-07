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

# environments
@pytest.fixture
def chrome_environment_setup():
        global driver
        driver= webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
    
         # ensure_all_first_requests_end
                                
def click(element):
       
        elementObject = driver.find_element(By.CSS_SELECTOR, element)
        
        if elementObject:
                driver.execute_script("arguments[0].click();", elementObject)
        else:
                print(fail_message)
                assert(False)

def click_by_xpath(element):
        
        elementObject = driver.find_element(By.XPATH, element)
        
        if elementObject:
                elementObject.click()
        else:
                print(fail_message)
                assert(False)

def quit_browser():
         
        driver.quit()