from environments import *
from assertDefinitions_pipeline import *
from Elements import *
from assertsByGroups import *

def test_research_development(chrome_environment_setup):

        #choice_categories
        choice_research_and_development()
        
        #end_test
        quit_browser()