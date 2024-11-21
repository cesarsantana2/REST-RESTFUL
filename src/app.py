from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados simulados
todos = [
    {"id": 1, "task": "Learn REST", "completed": False},
    {"id": 2, "task": "Build an API", "completed": True}
]

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
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if request.method == 'POST':
        todo['task'] = request.form['task']
        todo['completed'] = 'completed' in request.form
        return redirect(url_for('list_todos'))
    return render_template('update_todo.html', todo=todo)

@app.route('/todos/<int:todo_id>/delete', methods=['POST', 'GET'])
def delete_todo(todo_id):
    global todos
    if request.method == 'POST':
        todos = [t for t in todos if t["id"] != todo_id]
        return redirect(url_for('list_todos'))
    todo = next((t for t in todos if t["id"] == todo_id), None)
    return render_template('delete_todo.html', todo=todo)

if __name__ == '__main__':
    app.run(debug=True)
