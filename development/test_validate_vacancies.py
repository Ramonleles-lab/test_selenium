from environments import*
from assertDefinitions_pipeline import*
from assertsByGroups import*
import re
from Elements import *

def test_1(chrome_environment_setup):

        #comparing test
        locating_vacancies()

        #end_test
        quit_browser()