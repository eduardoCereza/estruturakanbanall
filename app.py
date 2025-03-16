#Importando biblioteca
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

#Lista de tarefas simulando um banco de dados simples
tasks = {
    "A fazer": ["Tarefa 1, Tarefa 2"],
    "Em progresso": ["Tarefa 3"],
    "Feito": ["Task 4"]
}

#Rota principal que renderiza o template
@app.route("/")
def index():
    return render_template('index.html', tasks=tasks)

#Rota para atualizar as tarefas
@app.route('/update_tasks', methods = ['POST'])
def update_tasks():
    global tasks
    new_tasks = request.json  # Dados enviados no corpo da requisição
    tasks = new_tasks         # Atualiza as tarefas com os novos dados
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)