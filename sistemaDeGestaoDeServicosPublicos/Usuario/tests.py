import unittest
from selenium import webdriver
# Create your tests here.

# pip install selenium
# python3.8 manage.py test

##### Função para realizar teste no formulário de cadastro de usuário #####

################### Teste de Cadastro ######################################
#class teste_cadastro_usuario(unittest.TestCase):
    #def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver.get('http://127.0.0.1:8000/Usuario/cadastrarUsuario/')

##### testando se a app está inserindo dados corretos para efetuar o cadastro #####
    #def teste_cadastro_correto(self):
        #self.usuario = self.driver.find_element_by_name("first_name")
        #self.usuario.send_keys("Roberto")
        #self.usuario = self.driver.find_element_by_name("last_name")
        #self.usuario.send_keys("Godoy da Silva")
        #self.usuario = self.driver.find_element_by_name("username")
        #self.usuario.send_keys("godoyRoberto@gmail.com")
        #self.usuario = self.driver.find_element_by_name("password1")
        #self.usuario.send_keys("testandoasenha123@")
        #self.usuario = self.driver.find_element_by_name("password2")
        #self.usuario.send_keys("testandoasenha123@")
        #self.usuario.submit()
        ##### relatorio===>>> Teste Funcionou!!! ##### 
    
    #def teste_cadastro_incorreto(self):
        #self.usuario = self.driver.find_element_by_name("first_name")
        #self.usuario.send_keys('Felipe')
        #self.usuario = self.driver.find_element_by_name("last_name")
        #self.usuario.send_keys("Servio")
        #self.usuario = self.driver.find_element_by_name("username")
        #self.usuario.send_keys("fsail")
        #self.usuario = self.driver.find_element_by_name("password1")
        #self.usuario.send_keys("testandoase3@")
        #self.usuario = self.driver.find_element_by_name("password2")
        #self.usuario.send_keys("testand")
        #self.usuario.submit()
        ###### relátorio==>>> os dados não podem ser salvos no banco se houver algum erro, teste funcionou!
    #def tearDown(self):
        #pass

##################Teste de Login #################################################
class teste_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/accounts/login/')

    # testando se a app está inserindo dados corretos para efetuar o login
    def teste_login_correto(self):
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
        #### bugs encontrados==>> quando o usuário digita a senha incorreta, não mostra nenhuma mensagem!

        self.usuario.submit()

    def tearDown(self):
        pass
        #self.driver.quit()
