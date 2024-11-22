from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Dados simulados (em memória)
todos = [
    {"id": 1, "task": "Learn REST", "completed": False},
    {"id": 2, "task": "Build an API", "completed": True}
]

# Helper para encontrar uma tarefa pelo ID
def find_todo(todo_id):
    return next((todo for todo in todos if todo["id"] == todo_id), None)

# ---------- ENDPOINTS HTML (FRONT-END) ----------

@app.route('/')
def home():
    return redirect(url_for('list_todos'))

@app.route('/todos')
def list_todos():
    return render_template('list_todos.html', todos=todos)

@app.route('/todos/new', methods=['GET', 'POST'])
def create_todo():
    if request.method == 'POST':
        task = request.form['task']
        completed = 'completed' in request.form
        new_todo = {"id": len(todos) + 1, "task": task, "completed": completed}
        todos.append(new_todo)
        return redirect(url_for('list_todos'))
    return render_template('create_todo.html')

@app.route('/todos/<int:todo_id>/edit', methods=['GET', 'POST'])
def update_todo(todo_id):
    todo = find_todo(todo_id)
    if not todo:
        return "Tarefa não encontrada", 404
    if request.method == 'POST':
        todo['task'] = request.form['task']
        todo['completed'] = 'completed' in request.form
        return redirect(url_for('list_todos'))
    return render_template('update_todo.html', todo=todo)

@app.route('/todos/<int:todo_id>/delete', methods=['POST', 'GET'])
def delete_todo(todo_id):
    global todos
    todo = find_todo(todo_id)
    if not todo:
        return "Tarefa não encontrada", 404
    if request.method == 'POST':
        todos = [t for t in todos if t["id"] != todo_id]
        return redirect(url_for('list_todos'))
    return render_template('delete_todo.html', todo=todo)

# ---------- ENDPOINTS API REST (JSON) ----------

@app.route('/api/todos', methods=['GET'])
def api_list_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def api_create_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "task": data.get("task"),
        "completed": data.get("completed", False)
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def api_update_todo(todo_id):
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    data = request.get_json()
    todo["task"] = data.get("task", todo["task"])
    todo["completed"] = data.get("completed", todo["completed"])
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def api_delete_todo(todo_id):
    global todos
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Tarefa excluída com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
