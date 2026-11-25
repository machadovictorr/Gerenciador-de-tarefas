import sqlite3 

conexao = sqlite3.connect("tarefas.db")
#função que conecta ao banco de dados
def conectar():
    conexao = sqlite3.connect("tarefas.db")
    return conexao

#função para criar a tabela de tarefas e que verifica se a tabela já existe
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        concluida INTEGER DEFAULT 0,
        criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    conexao.commit()
    conexao.close()

#função para inserir uma nova tarefa no banco de dados
def adicionar_tarefa(titulo, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)''', (titulo, descricao))
    id_tarefa = cursor.lastrowid

    conexao.commit()
    conexao.close()

#função para listar todas as tarefas no banco de dados
def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM tarefas''')
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas 

#função para atualizar uma tarefa no banco de dados
def atualizar_tarefa(id_tarefa, titulo, descricao, concluida):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''UPDATE tarefas SET titulo = ?, descricao = ?, concluida = ? WHERE id = ?''', (titulo, descricao, concluida, id_tarefa))
    
    conexao.commit()
    conexao.close()

#função para deletar uma tarefa no banco de dados
def deletar_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''DELETE FROM tarefas WHERE id = ?''', (id_tarefa,))
    conexao.commit()
    conexao.close()

