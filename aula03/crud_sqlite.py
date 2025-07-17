# crud

import sqlite3

# função conectar ao banco de dados (ou criar)
def conectar_banco():
    conexao = sqlite3.connect('exemplo.db') # nome do banco de dados
    return conexao


# função criar tabela no banco
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')    
    conexao.commit();
    conexao.close()
    print('--- Tabela usuarios criada!\n')


# função inserir dados na tabela
def inserir_usuario(nome, idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES(?, ?)
    ''', (nome, idade))    
    conexao.commit();
    conexao.close()
    print(f'Usuário: {nome}  Idade: {idade} inserido na tabela usuarios!\n')


# função listar dados
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
    ''')
    usuarios = cursor.fetchall()
    print('==== LISTANDO USUÁRIOS ====\n')
    for usuario in usuarios:
        print(usuario)    
    conexao.close()


# função atualizar dados
def atualizar_usuario(id, nome, idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios SET nome = ?, idade = ?
        WHERE id = ?
    ''', (nome, idade, id))    
    conexao.commit()
    conexao.close()
    print(f'Usuário: {nome} atualizado!\n')

# função excluir dados
def excluir_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE id = ?
    ''', (id,))    
    conexao.commit()
    conexao.close()
    print(f'Usuário: {id} excluído!\n')



# Criando a tabela
print('==== CRIANDO A TABELA ====\n')
criar_tabela()



# Inserindo dados na tabela
print('==== INSERINDO DADOS ====\n')
inserir_usuario('Caio', 31)
inserir_usuario('Jesreel', 21)
inserir_usuario('Eloara', 42)
inserir_usuario('Alice', 23)
inserir_usuario('Emily', 20)
inserir_usuario('Davi', 18)
inserir_usuario('Andressa', 51)
inserir_usuario('Teste', 100)



# Listando dados
listar_usuarios()



# Atualizando usuário
print('==== ATUALIZANDO USUARIO ====\n')
atualizar_usuario(2, 'Jesreel', 39)
listar_usuarios() # listar novamente os usuários apos atualizar



# Excluindo usuário
print('==== EXCLUINDO USUARIO ====\n')
excluir_usuario(8)
listar_usuarios() # listar novamente os usuários apos excluir
