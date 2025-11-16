from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import (
    ChromeDriverManager,
)
import time


def abrir_navegador_e_site(url: str):
    try:
        print("Configurando o serviço do ChromeDriver automaticamente...")
        servico = Service(ChromeDriverManager().install())

        print("Abrindo o navegador Chrome...")
        driver = webdriver.Chrome(service=servico)

        driver.maximize_window()
        print(f"Acessando o site: {url}")
        driver.get(url)
        return driver
    except Exception as e:
        print(f"Ocorreu um erro ao tentar abrir o navegador: {e}")
        return None

def clicar_botao_start(driver):
    try:
        time.sleep(1)
        print("Procurando o botão 'Start'...")
        xpath_do_botao = "//button[text()='Start']"
        botao_start = driver.find_element(By.XPATH, xpath_do_botao)
        print("Clicando no botão 'Start'...")
        botao_start.click()
        return True
    except Exception as e:
        print(f"Erro ao tentar clicar no botão 'Start': {e}")
        return False

def _preencher_campo_dinamico(driver, nome_do_campo: str, valor: str):
    try:
        xpath_dinamico = f"//label[text()='{nome_do_campo}']/following-sibling::input"
        campo = driver.find_element(By.XPATH, xpath_dinamico)
        campo.send_keys(str(valor)) 
        return True
    except Exception as e:
        print(
            f"Erro ao tentar preencher o campo '{nome_do_campo}'. Verifique o nome do campo e o XPath."
        )
        return False

def preencher_primeiro_nome(driver, valor: str):
    return _preencher_campo_dinamico(driver, "First Name", valor)

def preencher_ultimo_nome(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Last Name", valor)

def preencher_nome_empresa(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Company Name", valor)

def preencher_funcao(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Role in Company", valor)

def preencher_endereco(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Address", valor)

def preencher_email(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Email", valor)

def preencher_telefone(driver, valor: str):
    return _preencher_campo_dinamico(driver, "Phone Number", valor)

def clicar_submit(driver):
    
    try:
        botao_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        botao_submit.click()
        return True
    except Exception as e:
        print(f"Erro ao clicar em 'Submit': {e}")
        return False
