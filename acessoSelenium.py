"""
Professor,

Quando estou no meu computador normal, logado com a senha, o link abre direto:
http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/fcpj/consulta.asp

Porém ao abrir com driver...pede a senha toda vez e abre o recaptcha. O recaptcha detecta robo e me trava o código.
Não consigo passar o recaptcha.

O senhor pode acessar o link acima, informar o cpf '01303891026', e a senha: 'ZIP/DANI' e digitar esse protocolo expirado por exemplo "RSP1900282334"
Depois faça com meu script, verá que o site direciona para logar...sem ir direto para onde deveria ir, fazendo que eu chame duas vezes a mesma url.


Nota: eu uso (By.ID, ''), ESSE meu script é antigo pq eu desisti de tentar uma solução.
"""


import pdb
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os


def limpar_terminal():
    os.system('clear')


limpar_terminal()


print("Instanciando Driver")
driver = webdriver.Chrome()
driver.maximize_window()

print('Acessando URL')
driver.get(
    "http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/fcpj/consulta.asp")


print('Fazendo Login')
driver.find_element_by_id("j_username").clear()
driver.find_element_by_id("j_username").send_keys("01303891026")
driver.find_element_by_id("kc-login").click()

driver.find_element_by_id("j_password").clear()
driver.find_element_by_id("j_password").send_keys("ZIP/DANI")
sleep(3)
driver.find_element_by_id("submit-button").click()
sleep(20)

"""
Por causa desse rediciocionar para logar, abaixo tenho que chamar novamente o link inicial:
"""
driver.get(
    "http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/fcpj/consulta.asp")


sleep(2)
driver.find_element_by_id("prot").send_keys("RSP1900282334")


sleep(5)
print("Chrome fim.")
driver.close()
