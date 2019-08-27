import unittest
from selenium import webdriver
# Create your tests here.

# pip install selenium
# python3.8 manage.py test


# teste de login
class teste_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/accounts/login/')

    # testando se a app está inserindo dados corretos para efetuar o login
    def test_login_correto(self):
        self.usuario = self.driver.find_element_by_name("username")
        self.usuario.send_keys("admin")
        self.usuario = self.driver.find_element_by_name("password")
        self.usuario.send_keys("admin")

        self.usuario.submit()

    # testando se a app está inserindo dados errados para efetuar o login
    def teste_login_incorreto(self):
        self.usuario = self.driver.find_element_by_name("username")
        self.usuario.send_keys("uytret")
        self.usuario = self.driver.find_element_by_name("password")
        self.usuario.send_keys("hjbkço")
        # bugs encontrados==>> quando o usuário digita a senha incorreta, não mostra nenhuma mensagem!
        # bugs corrigido

        self.usuario.submit()

    def tearDown(self):
        pass
        self.driver.quit()
