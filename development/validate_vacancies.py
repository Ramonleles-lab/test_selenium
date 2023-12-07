from environments import *
from assertDefinitions_pipeline import *
from Elements import *
from assertsByGroups import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# Abre a página de vagas e maximiza a janela do navegador
driver.get("https://cz.careers.veeam.com/vacancies")
driver.maximize_window()
#choice_vacancy
numero_de_vagas = len(driver.find_elements(By.PARTIAL_LINK_TEXT,"Prague" ))
resultado_esperado = 16

if numero_de_vagas == resultado_esperado:
                print("Número de vagas está correto!")
else:
                print(f"Erro: Número de vagas encontrado ({numero_de_vagas}) é diferente do resultado esperado ({resultado_esperado}).")

driver.quit()