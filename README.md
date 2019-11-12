Instalando a virtualenv
A instalação de uma virtualenv é feita utilizando o pip, gerenciador de pacotes do Python. Após instalar o pip, utilizamos o comando abaixo para instalar o pacote virtualenv em nosso computador:

pip install virtualenv

Feito isso, o pacote estará instalado e pronto para ser utilizado. Agora já podemos criar e gerenciar nossos ambientes virtuais.

Criando uma nova virtualenv
O processo de criação de uma virtualenv é bastante simples e pode ser feito utilizando um único comando, como podemos ver abaixo:

virtualenv nome_da_virtualenv

O mais comum é criar a virtualenv na raiz do projeto que ela irá pertencer. Isso permite uma organização maior das virtualenvs que possuímos em nosso computador:

Com isso, criamos a virtualenv do projeto chamada “venv”. É ela quem vai comportar todos os pacotes necessários para a execução do projeto.

Ativando uma virtualenv
Após criar uma virtualenv, precisamos ativá-la para que possamos instalar os pacotes necessários do projeto. Para isso, utilizamos o seguinte comando:

source nome_da_virtualenv/bin/activate (Linux ou macOS)

ou

nome_da_virtualenv\Scripts\activate (Windows)

O comando acima irá ativar a virutalenv e teremos um retorno similar ao ilustrado abaixo:

Note que o nome da virtualenv, agora, é exibido antes do caminho do diretório em que estamos. Isso indica que a virtualenv foi ativada com sucesso.

Desativando uma virtualenv
Para desativar uma virtualenv utilizamos o comando desactivate.

Instalando pacotes
Com a virtualenv ativada, podemos instalar os pacotes necessários do projeto utilizando o próprio PIP. Agora, instalamos o pacote Django, em sua versão mais atual, na virtualenv do projeto “projeto_python”. Agora, se precisarmos instalar uma outra versão do Django em outro projeto, bastaria criar uma nova virtualenv e realizar o mesmo processo.

Essas e outras dicas eu encontrei no site TreinaWeb
Aprendendo Django


instalar selenium web driver
pip install selenium

executar o servidor local
python3.8 manage.py test

importações selenium
import unittest
from selenium import webdriver







