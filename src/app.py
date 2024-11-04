from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Funções para carregar e salvar tarefas em um arquivo JSON
def load_todos():
    if os.path.exists('todos.json'):
        with open('todos.json', 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open('todos.json', 'w') as file:
        json.dump(todos, file, indent=4)

# Carregar tarefas iniciais do arquivo JSON
todos = load_todos()

# Endpoint para listar todas as tarefas (GET)
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Endpoint para criar uma nova tarefa (POST)
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.json
    new_todo['id'] = len(todos) + 1  # Geração simples de ID
    todos.append(new_todo)
    save_todos(todos)  # Salvar no arquivo após criar uma nova tarefa
    return jsonify(new_todo), 201

# Endpoint para atualizar uma tarefa (PUT)
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo.update(request.json)
    save_todos(todos)  # Salvar no arquivo após a atualização
    return jsonify(todo)

# Endpoint para deletar uma tarefa (DELETE)
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)  # Salvar no arquivo após deletar uma tarefa
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
