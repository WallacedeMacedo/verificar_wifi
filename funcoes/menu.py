from funcoes.bot import Bot
import os


class Menu:

    def __init__(self):
        self.controle()

    @staticmethod
    def controle():
        bot = Bot()
        bot.abrir_navergador()
        bot.acessar_lista_negra()
        os.system('cls')
        bot.lista_dispositivos()
        bot.bloquear_desbloquear()
        bot.sair()
