# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

"""
Crie primeiro um profile salvando a senha.
https://support.mozilla.org/pt-BR/kb/gerenciador-de-perfis-crie-remova-ou-troque-perfis?redirectlocale=pt-BR&redirectslug=gerenciador-de-perfis-para-criar-remover-perfis
"""

dir = 'C:\Users\ReinaldoRossettii\AppData\Roaming\Mozilla\Firefox\Profiles\878rtczp.reinaldo'
firefox_profile = webdriver.FirefoxProfile(profile_directory=dir)
driver = webdriver.Firefox(firefox_profile=firefox_profile)

driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(60)
driver.set_script_timeout(5)

# carrega a pagina com a sessao salva no profile
driver.get("https://areadousuario.redesim.gov.br/")
# precisa de um tempo pra carregar os cookies, se for muito rapido ele te redireciona.
sleep(5)
# muda a pagina sem apagar os cookies
driver.execute_script("window.location='http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/fcpj/consulta.asp'")
sleep(5)
# inserindo os dados via javascript
driver.execute_script('document.querySelector("#prot").value="RSP1900282334"')
sleep(5)
driver.close()
