from flask import Flask, redirect, url_for, request, render_template
from requests import get

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('inicio.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/pagina403')
def pagina403():
    return render_template('pagina403.html')


@app.route('/validador', methods=['POST','GET']) # aceita POST ou GET
def validador():
    acesso_usuario = 'jesreel'
    acesso_senha = '123'

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == acesso_usuario and senha == acesso_senha:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))

    else:
        usuario = request.args.get('usuario')
        senha = request.args.get('senha')
        if usuario == acesso_usuario and senha == acesso_senha:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))




# Iniciar Servidor
if __name__ == '__main__':
    app.run(debug = True)
    #app.run('0.0.0.0') # faz rodar o localhost