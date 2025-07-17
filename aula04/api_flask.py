# Criar api usando flask

# importar biblioteca Flask
from flask import Flask, render_template


# Criar app flask
app = Flask(__name__)

# Rota da pagina principal 
'''
@ é um decorator. tudo que vier embaixo
é um argumento e faz parte do route
'''
@app.route('/')
def home():
    return "<h1>Flask API: [home]</h1>"


@app.route('/sobre')
def sobre():
    return "<h1>Flask API: [sobre]</h1>"


# Rota com variáveis na url
@app.route('/api/v1/<nome>')
def retorna_nome(nome):
    return f"<h1> Olá, {nome}!</h1><h2><i>Seja bem vindo.</i></h2><br /><a href='https://github.com/jesreel' target='_blank'>Acesso ao Github</a>"



# Iniciar Servidor
if __name__ == '__main__':
    app.run(debug = True)



