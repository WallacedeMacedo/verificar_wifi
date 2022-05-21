import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from funcoes.login import Credencial


class Bot:

    def __init__(self):

        self.bot = Credencial()
        self.no = ''
        self.host = ''
        self.mac = ''

    def abrir_navergador(self):
        try:
            self.bot.driver.get('http://192.168.0.1/index.html#home')
            wait = WebDriverWait(self.bot.driver, timeout=10, poll_frequency=1, ignored_exceptions=[
                ElementNotVisibleException, ElementNotSelectableException])
            wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div['
                                                                   '2]/div/div/form[1]/div[2]/div[2]/input')))
            self.bot.fazer_login()
        except InvalidSessionIdException:
            # print('Página não está respondendo. '+ str(e))
            print('Página não está respondendo.')
        except TimeoutException:
            # print('Tempo de carregamento da página foi atingido. ' + str(e))
            print('Tempo de carregamento da página foi atingido.')
        # finally:
        #     self.sair()
        #     time.sleep(5)
        #     self.bot.driver.close()

    def exibir_dispositivos(self):
        dicionario_dispositivos = {}
        contador = 0
        try:
            for contador in range(1, 5, 1):

                time.sleep(1)

                no = self.no.replace('contador', str(contador))
                host = self.host.replace('contador', str(contador))
                mac = self.mac.replace('contador', str(contador))

                dicionario_dispositivos['no'] = self.bot.driver.find_element(by=By.XPATH, value=no).text
                dicionario_dispositivos['host'] = self.bot.driver.find_element(by=By.XPATH, value=host).text
                dicionario_dispositivos['mac'] = self.bot.driver.find_element(by=By.XPATH, value=mac).text

                print(f"{'Posição: ' + dicionario_dispositivos['no']:<3}  "
                      f"{'Nome: ' + dicionario_dispositivos['host']:<16}  "
                      f"{'Mac: ' + dicionario_dispositivos['mac']:>17} ")
            return 1

        except NoSuchElementException:
            # print(e.screen) = None
            # print(e.msg)
            if contador - 1 == 0:
                print(contador - 1)
            return 0

    def acessar_lista_negra(self):

        wait = WebDriverWait(self.bot.driver, timeout=10, poll_frequency=1, ignored_exceptions=[
            ElementNotVisibleException, ElementNotSelectableException])
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/ul/li[5]/a')))

        time.sleep(3)
        # Clicando no botão "Configurações"
        self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/ul/li[5]/a').click()

        time.sleep(3)
        # Clicando no botão "Configurações Wi-Fi"
        self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[1]/ul/li[5]/a').click()

        time.sleep(3)
        # Clicando no botão "Lista estações"
        self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[1]/ul/li[6]/ul/li[3]/a').click()

    def lista_dispositivos(self):
        try:
            # Exibir dispositivos conectados
            print('Conectados: ')
            self.no = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[' \
                      'contador]/td[1] '
            self.host = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[' \
                        'contador]/td[2] '
            self.mac = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[2]/table/tbody/tr[' \
                       'contador]/td[3] '
            self.exibir_dispositivos()
            print()
            print('Bloqueados: ')
            # Exibir dispositivos bloquados
            self.no = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[contador]/td[1]'
            self.host = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[' \
                        'contador]/td[2] '
            self.mac = '/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div[3]/div[1]/div/table/tbody/tr[' \
                       'contador]/td[3] '
            self.exibir_dispositivos()
            print()
        except NoSuchElementException:
            print('Caminho não encontrado. Por favor, verifique o valor informado.')

    def bloquear_desbloquear(self):

        while True:
            print('Escolha uma das opções: ')
            print('1 - Bloquear')
            print('2 - Desbloquear')
            print('3 - Sair')
            opcao = input('opcao: ')

            if opcao == '1':
                dispositivo = input('Informe a posição do dispositivo a ser bloqueado: ')
                self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div['
                                                                '3]/div[2]/div[2]/table/tbody/tr[{}]/td['
                                                                '4]/input'.format(dispositivo)).click()
                print('Dispositivo bloqueado!')
                return 1
            elif opcao == '2':
                dispositivo = input('Informe a posição do dispositivo a ser desbloqueado: ')
                self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[2]/form/div/div['
                                                                '3]/div[1]/div/table/tbody/tr[{}]/td[4]'.format(
                                                                 dispositivo)).click()
                print('Dispositivo desbloqueado!')
                return 1
            else:
                print('Opção inválido.')
                return 0

    def sair(self):
        try:
            print('Saindo...')
            time.sleep(2)

            # Clicando no botão "Sair"
            self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[2]/div/span[2]/a').click()

            time.sleep(3)
            # Clicando no botão "Sim"
            self.bot.driver.find_element(by=By.XPATH, value='/html/body/div[8]/div/div/div[5]/input[2]').click()

            time.sleep(3)
            self.bot.driver.close()

        except ElementClickInterceptedException:
            print('O comando Element Click não pôde ser concluído porque o elemento que recebe os eventos está '
                  'obscurecendo o elemento que foi solicitado para ser clicado.')
        except NoSuchElementException:
            print('Botão "Sair" não foi encontrado.')
