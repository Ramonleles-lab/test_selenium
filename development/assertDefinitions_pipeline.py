import pytest
import time
from environments import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from environments import *
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Elements import *
from selenium.webdriver.common.keys import Keys
import re

fail_message = "fail_message"

# environments
@pytest.fixture
def chrome_environment_setup():
        global driver
        driver= webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()


def locating_vacancies():
        
        #choice_vacancy
        number_of_vacancies = len(driver.find_elements(By.PARTIAL_LINK_TEXT,Elements.vacancies_found ))

        # Find the element containing the text with the dynamic number
        element = driver.find_element(By.TAG_NAME,Elements.vacancies_open)

        # Get element text
        text_advertised_acancies = element.text

        # regular expression to extract the number
        vacancies_extracted = int(re.search(r'\d+', text_advertised_acancies).group())

        # print number of vacancies
        print(f"vacancies extracted: {vacancies_extracted}")

        if number_of_vacancies == vacancies_extracted:
                
            print("Number of vacancies is correct!")
        else:
            print(f"Error: Number of vacancies found ({number_of_vacancies}) is different from the expected result ({vacancies_extracted}).")

        driver.quit()
                                
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