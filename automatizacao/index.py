from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get('https://marigsiqueira.github.io/Leilao-TesteAutomatizado/')

def testar_lance(valor_lance):
    input_lance = driver.find_element(By.ID, "valor-lance")
    input_lance.clear()

    input_lance.send_keys(str(valor_lance))

    botao_enviar = driver.find_element(By.XPATH, "//button[contains(text(),'Enviar')]")
    botao_enviar.click()

    time.sleep(2)

    alerta = driver.find_element(By.ID, "alerta")
    return alerta.text

mensagem = testar_lance(300)
print(f"Teste 1 (lance < 450): {mensagem}")
assert mensagem == "O lance mínimo é R$450,00", "Mensagem de erro não exibida corretamente!"

mensagem = testar_lance(500)
print(f"Teste 2 (lance >= 450): {mensagem}")
assert "Lance de R$500.00 enviado com sucesso!" in mensagem, "Mensagem de sucesso não exibida corretamente!"

driver.quit()
