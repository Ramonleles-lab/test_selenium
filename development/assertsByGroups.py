from assertDefinitions_pipeline import *
from Elements import *
from selenium.webdriver.common.keys import Keys
import re

def choice_research_and_development():
        click(Elements.all_departaments)
        click_by_xpath(Elements.research_and_development)