import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

try:
    #driver = webdriver.Chrome('C:\driver_chrome\chromedriver.exe')
    #driver = webdriver.Edge('C:\driver_edge\msedgedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #driver.set_page_load_timeout(10)
    url = 'http://192.168.0.1/index.html#home'
    driver.get(url)
except InvalidSessionIdException as e:

    print("Tempo de carregamento da página foi atingido. " + str(e))
    driver.close()
#except TimeoutException as e:
#    e

try:
    time.sleep(5)
    # Campos usuário e senha e inserindo os dados.
    usuario = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/div/div/form[1]/div[2]/div[2]/input')
    usuario.send_keys('CLARO_713CD8')
    senha = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/div/div/form[1]/div[3]/div[2]/input')
    senha.send_keys('B41C30713CD8')

    time.sleep(3)
    # Clicando no botão "Entrar"
    driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/div/div/form[1]/div[4]/div[2]/input').click()
except NoSuchElementException as e:
    e

time.sleep(5)
# Clicando no botão "Configurações"
driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[2]/ul/li[5]/a').click()

time.sleep(5)
# Clicando no botão "Configurações Wi-Fi"
driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[1]/ul/li[5]/a').click()

time.sleep(5)
# Clicando no botão "Lista estações"
driver.find_element(by=By.XPATH,value='//*[@id="leftmenu"]/li[6]/ul/li[3]/a').click()

os.system('cls')
# Verificando dispositivos conectados
print('Dispositivos conectado(s): ')
qtd_conectados = 0
try:
    for i in range(5):
        i += 1
        time.sleep(1)
        no_conectado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[1]'.format(i))
        host_conectado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[2]'.format(i))
        mac_conectado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[3]'.format(i))
        qtd_conectados += 1
        # print('Número: ' + no.text)
        # print('Dispositivo: ' + host.text)
        # print('Mac: ' + endereco_mac.text)
        print('Número: ' + no_conectado.text + '; ', 'Dispositivo: ' + host_conectado.text + '; ',
              'Mac: ' + mac_conectado.text)
except NoSuchElementException as e:
    e

print('\n')
# Verificando dispositivos bloqueados
print('Dispositivos bloqueado(s): ')
try:
    qtd_bloqueados = 0
    for i in range(4):
        i += 1
        time.sleep(1)
        no_bloqueado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[{}]/td[1]'.format(i))
        host_bloqueado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[{}]/td[2]'.format(i))
        mac_bloqueado = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[{}]/td[3]'.format(i))

        print('Número: ' + no_bloqueado.text + '; ', 'Dispositivo: ' + host_bloqueado.text + '; ',
              'Mac: ' + mac_bloqueado.text)
except NoSuchElementException as e:
    e
    if (i - 1 == 0):
        print(i - 1)

print('\n')

while True:
    opcao = 0
    print('Escolha uma das opções: ')
    print('1 - Bloquear')
    print('2 - Desbloquear')
    print('3 - Sair')
    opcao = input('opcao: ')

    if (opcao == '1'):
        dispositivo = input('Informe a posição do dispositivo a ser bloqueado: ')
        driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[4]/input'.format(dispositivo)).click()
        print('Dispositivo bloqueado!')
        # print('Dispositivo ' + str(host_conectado.text) + ' - ' + str(mac_conectado.text) + ' bloqueado!') - criar lista para incrementar p/ utilizar está linha

        break
    elif (opcao == '2'):
        dispositivo = input('Informe a posição do dispositivo a ser desbloqueado: ')
        driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[{}]/td[4]'.format(dispositivo)).click()
        print('Dispositivo desbloqueado!')
        # print('Dispositivo ' + str(host_bloqueado.text) + ' - ' + str(mac_bloqueado.text) + ' desbloqueado!')
        break
    elif (opcao == '3'):
        break
    else:
        print('Opção inválido.')

print('Saindo...')
time.sleep(5)
# Clicando no botão "Sair"
driver.find_element(by=By.XPATH, value='//*[@id="logoutlink"]').click()

time.sleep(2)
# Clicando no botão "Sim"
driver.find_element(by=By.XPATH, value='//*[@id="yesbtn"]').click()

time.sleep(3)
# Fechando o navegador.
driver.close()
