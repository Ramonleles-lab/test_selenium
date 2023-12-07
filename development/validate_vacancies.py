from environments import *
from Elements import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()

# Open the jobs page and maximize the browser window
driver.get(url)
driver.maximize_window()

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