<h3>Instalando a virtualenv</h3>
A instalação de uma virtualenv é feita utilizando o pip, gerenciador de pacotes do Python. Após instalar o pip, utilizamos o comando abaixo para instalar o pacote virtualenv em nosso computador:

<strong>pip install virtualenv</strong>

Feito isso, o pacote estará instalado e pronto para ser utilizado. Agora já podemos criar e gerenciar nossos ambientes virtuais.

<h3>Criando uma nova virtualenv</h3>
O processo de criação de uma virtualenv é bastante simples e pode ser feito utilizando um único comando, como podemos ver abaixo:

<strong>virtualenv nome_da_virtualenv</strong>

O mais comum é criar a virtualenv na raiz do projeto que ela irá pertencer. Isso permite uma organização maior das virtualenvs que possuímos em nosso computador:

Com isso, criamos a virtualenv do projeto chamada “venv”. É ela quem vai comportar todos os pacotes necessários para a execução do projeto.

<h3>Ativando uma virtualenv</h3>
Após criar uma virtualenv, precisamos ativá-la para que possamos instalar os pacotes necessários do projeto. Para isso, utilizamos o seguinte comando:

<strong>source nome_da_virtualenv/bin/activate (Linux ou macOS)</strong>

ou

<strong>nome_da_virtualenv\Scripts\activate (Windows)</strong>

O comando acima irá ativar a virutalenv e teremos um retorno similar ao ilustrado abaixo:

Note que o nome da virtualenv, agora, é exibido antes do caminho do diretório em que estamos. Isso indica que a virtualenv foi ativada com sucesso.

<h3>Desativando uma virtualenv</h3>
Para desativar uma virtualenv utilizamos o comando <strong>deactivate</strong>.

<h3>Instalando pacotes</h3>
Com a virtualenv ativada, podemos instalar os pacotes necessários do projeto utilizando o próprio PIP. Agora, instalamos o pacote Django, em sua versão mais atual, na virtualenv do projeto “projeto_python”. Agora, se precisarmos instalar uma outra versão do Django em outro projeto, bastaria criar uma nova virtualenv e realizar o mesmo processo.

Essas e outras dicas encontra-se nos sites <a href="https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/">TreinaWeb</a>  e <a href="https://data-flair.training/blogs/django-architecture/">Aprendendo Django</a>


<h3>instalar selenium web driver(Ambiente de teste)</h3>
<strong>pip install selenium</strong>

<h3>executar o servidor local</h3>
<strong>python manage.py test</strong>

<h3>Importações selenium necessárias</h3>
<strong>import unittest</strong>
<strong>from selenium import webdriver</strong>







