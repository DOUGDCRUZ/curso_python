'''
No terminal:
* Instalar a biblioteca/módulo: pip install flask
* Verificar a versão: flask --version
* Se necessário, atualizar: pip install --upgrade flask
* pip freeze > requirements.txt # criar arquivo requirements com todas as saídas do pip freeze
'''

from flask import Flask, render_template

app = Flask('Hello')   #Flask é uma classe

@app.route('/hello')    #criar uma rota => página WEB com nome hello
def hello():
    return render_template('hello.html')
@app.route('/tchau')    #criar uma rota => página WEB com nome hello
def tchau():
    return 'tchau'

'''
Para atualizar automaticamente as alterações no código faça as alteraçõea abaixo
No terminal:
pip install python-dotenv # envia as varíaveis de configuração contidas no arquivo .flaskenv
pip freeze > requirements.txt # criar o arquivo com todas as bibliotecas instaladas durante o desenvolvimento
echo $USER # variável do ambiente($) => nome do usuário
echo $HOME
echo $PATH # o caminho de todos os arquivos executáveis da máquina

Criar um novo arquivo de configuração com nome (começa com ponto porque ele é oculto): .flaskenv


git add .
git commit -m 'aula 1'
git push
'''