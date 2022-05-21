from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import InvalidSessionIdException
import time


class Credencial:
    def __init__(self):

        self.__usuario = ''
        self.__senha = ''
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def fazer_login(self):
        
        try:
            # Campos usuário e senha e inserindo os dados.
            usuario = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div['
                                                                  '2]/div/div/form[1]/div[2]/div[2]/input')
            usuario.send_keys(self.__usuario)
            senha = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[2]/div/div/form['
                                                                '1]/div[3]/div[2]/input')
            senha.send_keys(self.__senha)

            time.sleep(2)
            # Clicando no botão "Entrar"
            self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[1]/div[2]/div/div/form[1]/div['
                                                        '4]/div[2]/input').click()
            return 1
        except NoSuchElementException as e:
            print('Elemento não encontrado na página' + str(e))
            return 0
