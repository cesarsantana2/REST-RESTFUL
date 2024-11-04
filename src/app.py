from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais de exemplo
todos = [
    {"id": 1, "task": "Learn REST", "completed": False},
    {"id": 2, "task": "Build an API", "completed": False}
]

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
    return jsonify(new_todo), 201

# Endpoint para atualizar uma tarefa (PUT)
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo.update(request.json)
    return jsonify(todo)

# Endpoint para deletar uma tarefa (DELETE)
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)

