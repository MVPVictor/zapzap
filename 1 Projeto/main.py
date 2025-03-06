# para importar use o comando ( "pip install ..." ) no command prompt e depois importa no python
# site com os scripts : https://cdnjs.com/
#websocket -> tunel para duas pessoas acessarem juntas

# PASSO 1 PENSAR QUAL TIPO DE SITE QUE VOU FAZER

# WHATS
# VENDAS COM CHAT PRA AJUDA
# SITE DE ARMAZENAMENTO DE DADOS

# PASSO 2 CRIAR O SITE

# PASSO 3 CRIAR CHAT DE RESPOSTA

# PASSO 4 FAZER ENTRAR NELE

# PASSO 5 FAZER O LOGIN NELE

# PASSO 6 REVER AS FUNCIONALIDADES E VER PASSO POR PASSO PARA VER SE NÃO TEM PROBLEMA

# PASSO 7 PEGAR IDEIAS COM PESSOAS DIVERSAS

# PASSO 8 INCREMENTAR AS IDEIAS NO SITE

# PASSO 9 REVER TANTO BACK QUANTO FRONT

# PASSO 10 FAZER O TESTE PESSOALMENTE

# PASSO 11 FAZER COM QUE FUNCIONE COM O @MEDIA PARA QUE FUNCIONE TANTO PARA COMPUTADOR QUANTO PARA TELEFONE

# PASSO 12 FAZER O TESTE POR TELEFONE PESSOALMENTE

# PASSO 13 DEIXA OUTRA PESSOA TESTAR TANTO POR TELEFONE QUANTO PELO COMPUTADOR

# TIRAR MODO debug=true
# Sempre instalar com (pip install flask) (pip install flask_socketio) e etc toda vez que trocar de maquina

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

@app.route("/")
def homepage():
    return render_template("homepage.html")

socketio.run(app, debug=True, host="192.168.1.10")
#Toda vez que for trocar de internet colocar o ip da internet no lugar